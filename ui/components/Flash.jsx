import React, { useState } from "react";

export default function Flash() {

  const [progress, setProgress] = useState(0);
  const [speed, setSpeed] = useState(0);
  const [status, setStatus] = useState("");

  const iso = "/etc/hosts";
  const device = "/dev/sdb";

  const startFlash = async () => {

    const sizeRes = await fetch(`http://127.0.0.1:8000/iso-size?path=${iso}`);
    const { size } = await sizeRes.json();

    const res = await fetch("http://127.0.0.1:8000/flash", {
      method: "POST",
      headers: {"Content-Type":"application/json"},
      body: JSON.stringify({ iso, device })
    });

    const reader = res.body.getReader();
    const decoder = new TextDecoder();

    let received = 0;

    while (true) {
      const { done, value } = await reader.read();
      if (done) break;

      const chunk = decoder.decode(value);
      const lines = chunk.split("\n");

      for (let line of lines) {
        if (!line) continue;

        const data = JSON.parse(line);

        if (data.bytes) {
          received = data.bytes;

          setProgress((received / size) * 100);
          setSpeed(data.speed.toFixed(1));
        }

        if (data.status === "done") {
          setStatus("🔍 Verifying...");
        }

        if (data.status === "aborted") {
          setStatus("🛑 Aborted");
        }

        if (data.verify) {
          if (data.verify.fast.match) {
            setStatus("✅ Done & Verified");
          } else {
            setStatus("❌ Verify Failed");
          }
        }
      }
    }
  };

  const stop = async () => {
    await fetch("http://127.0.0.1:8000/abort", { method: "POST" });
  };

  return (
    <div>
      <button onClick={startFlash}>🔥 Flash</button>
      <button onClick={stop}>🛑 Stop</button>

      <p>Progress: {progress.toFixed(1)}%</p>
      <p>Speed: {speed} MB/s</p>
      <p>{status}</p>
    </div>
  );
}
