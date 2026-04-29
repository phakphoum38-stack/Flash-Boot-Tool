import React, { useState } from "react";

export default function BootEmulator() {

  const [result, setResult] = useState("");
  const [log, setLog] = useState("");

  const iso = "/home/phakphum/test.iso";

  const runTest = async () => {

    const res = await fetch("http://127.0.0.1:8000/boot-test", {
      method: "POST",
      headers: {"Content-Type":"application/json"},
      body: JSON.stringify({ iso })
    });

    const data = await res.json();

    setResult(data.result.status + " - " + data.result.reason);
    setLog(data.log);
  };

  return (
    <div>
      <button onClick={runTest}>🧪 Test Boot</button>

      <p>Result: {result}</p>

      <pre style={{maxHeight:200, overflow:"auto"}}>
        {log}
      </pre>
    </div>
  );
}
