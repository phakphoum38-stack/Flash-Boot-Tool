import { useState } from "react";

export default function ProgressBar({ iso, device }) {

  const [progress, setProgress] = useState(0);
  const [speed, setSpeed] = useState(0);
  const [eta, setEta] = useState(0);
  const [text, setText] = useState("");

  const start = async () => {

    // 🔥 ดึงขนาด ISO จริง
    const res = await fetch(`http://localhost:8000/iso-size?path=${iso}`);
    const { size: totalSize } = await res.json();

    const evt = new EventSource(
      `http://localhost:8000/flash-progress?iso=${iso}&device=${device}`
    );

    evt.onmessage = (e) => {
      const data = JSON.parse(e.data);

      if (data.status === "done") {
        setText("✅ Done");
        evt.close();
        return;
      }

      const percent = (data.bytes / totalSize) * 100;

      // 🔥 ETA คำนวณตรงนี้
      const remainingBytes = totalSize - data.bytes;
      const bytesPerSec = data.speed * 1024 * 1024; // MB/s → bytes/s
      const etaSeconds = remainingBytes / bytesPerSec;

      setProgress(percent.toFixed(2));
      setSpeed(data.speed);
      setEta(etaSeconds);
      setText(`${percent.toFixed(1)}%`);
    };
  };

  // 🔥 แปลง ETA ให้อ่านง่าย
  const formatTime = (sec) => {
    if (!sec || sec === Infinity) return "--";

    const m = Math.floor(sec / 60);
    const s = Math.floor(sec % 60);

    return `${m}m ${s}s`;
  };

  return (
    <div style={{ marginTop: 20 }}>
      <button onClick={start}>Start Flash</button>

      {/* Progress bar */}
      <div style={{
        width: "100%",
        height: 20,
        background: "#333",
        borderRadius: 10,
        marginTop: 10
      }}>
        <div style={{
          width: `${progress}%`,
          height: "100%",
          background: "#0a84ff",
          borderRadius: 10,
          transition: "width 0.3s ease"
        }} />
      </div>

      <p>{text}</p>
      <p>⚡ {speed} MB/s</p>
      <p>⏱ ETA: {formatTime(eta)}</p>
    </div>
  );
}
