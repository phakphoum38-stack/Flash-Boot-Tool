import React, { useState } from "react";
import DropZone from "./components/DropZone";
import DeviceSelect from "./components/DeviceSelect";
import ProgressBar from "./components/ProgressBar";
import { streamJSONLines } from "./utils/stream";

const API = "http://127.0.0.1:8000";

export default function App() {

  const [iso, setIso] = useState("");
  const [device, setDevice] = useState("/dev/sdb");

  const [log, setLog] = useState("");
  const [result, setResult] = useState("");

  const [progress, setProgress] = useState(0);
  const [speed, setSpeed] = useState(0);
  const [status, setStatus] = useState("");

  // 🧪 Boot Emulator
  const testBoot = async () => {
    const res = await fetch(`${API}/boot-test`, {
      method: "POST",
      headers: {"Content-Type":"application/json"},
      body: JSON.stringify({ iso })
    });

    const data = await res.json();
    setLog(data.log);
    setResult(JSON.stringify(data.result));
  };

  // 🧠 AI Analyze
  const analyze = async () => {
    const res = await fetch(`${API}/auto-fix`, {
      method: "POST",
      headers: {"Content-Type":"application/json"},
      body: JSON.stringify({ log, device })
    });

    const data = await res.json();
    setResult(JSON.stringify(data, null, 2));
  };

  // 🔥 Flash + Verify
  const startFlash = async () => {

    const sizeRes = await fetch(`${API}/iso-size?path=${iso}`);
    const { size } = await sizeRes.json();

    const res = await fetch(`${API}/flash`, {
      method: "POST",
      headers: {"Content-Type":"application/json"},
      body: JSON.stringify({ iso, device })
    });

    await streamJSONLines(res, (data) => {

      if (data.bytes) {
        setProgress((data.bytes / size) * 100);
        setSpeed(data.speed.toFixed(1));
      }

      if (data.status === "done") {
        setStatus("🔍 Verifying...");
      }

      if (data.verify) {
        setStatus(
          data.verify.fast.match
            ? "✅ Done & Verified"
            : "❌ Verify Failed"
        );
      }
    });
  };

  // 🛑 Kill switch
  const stop = async () => {
    await fetch(`${API}/abort`, { method: "POST" });
    setStatus("🛑 Aborted");
  };

  return (
    <div style={{ maxWidth: 700, margin: "auto", padding: 20 }}>

      <h2>🔥 Flash Boot Tool AI</h2>

      <DropZone setIso={setIso} />
      <p>ISO: {iso}</p>

      <DeviceSelect device={device} setDevice={setDevice} />

      <hr />

      <button onClick={testBoot}>🧪 Test Boot</button>
      <button onClick={analyze}>🧠 Analyze</button>
      <button onClick={startFlash}>🔥 Flash</button>
      <button onClick={stop}>🛑 Stop</button>

      <hr />

      <ProgressBar percent={progress} />
      <p>⚡ {speed} MB/s</p>
      <p>{status}</p>

      <h4>Result</h4>
      <pre>{result}</pre>

      <h4>Boot Log</h4>
      <pre style={{ maxHeight: 200, overflow: "auto" }}>{log}</pre>

    </div>
  );
}
