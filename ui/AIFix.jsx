import React, { useState } from "react";

export default function AIFix() {

  const [log, setLog] = useState("");
  const [result, setResult] = useState("");

  const device = "/dev/sdb";

  const analyze = async () => {
    const res = await fetch("http://127.0.0.1:8000/auto-fix", {
      method: "POST",
      headers: {"Content-Type":"application/json"},
      body: JSON.stringify({ log, device })
    });

    const data = await res.json();
    setResult(JSON.stringify(data, null, 2));
  };

  const apply = async () => {
    const res = await fetch("http://127.0.0.1:8000/apply-fix", {
      method: "POST",
      headers: {"Content-Type":"application/json"},
      body: JSON.stringify({ log, device })
    });

    const data = await res.json();
    setResult(JSON.stringify(data, null, 2));
  };

  return (
    <div>
      <textarea onChange={(e)=>setLog(e.target.value)} />

      <button onClick={analyze}>🧠 Analyze</button>
      <button onClick={apply}>🔧 Apply Fix</button>

      <pre>{result}</pre>
    </div>
  );
}
