import { useState } from "react";

export default function ProgressBar({ iso, device }) {

  const [progress, setProgress] = useState(0);
  const [speed, setSpeed] = useState(0);
  const [text, setText] = useState("");

  const start = () => {

    const totalSize = 4 * 1024 * 1024 * 1024; // TODO: replace with real ISO size

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

      setProgress(percent.toFixed(2));
      setSpeed(data.speed);
      setText(`${percent.toFixed(1)}%`);
    };
  };

  return (
    <div style={{ marginTop: 20 }}>
      <button onClick={start}>Start Flash</button>

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
          borderRadius: 10
        }} />
      </div>

      <p>{text}</p>
      <p>⚡ {speed} MB/s</p>
    </div>
  );
}
