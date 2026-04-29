import React from "react";

export default function Verify({ iso, device }) {

  const runVerify = async () => {
    const res = await fetch("http://localhost:8000/verify", {
      method: "POST",
      headers: {"Content-Type":"application/json"},
      body: JSON.stringify({ iso, device })
    });

    const data = await res.json();

    if (data.full) {
      alert(`FULL VERIFY: ${data.full.match ? "OK" : "FAIL"}`);
    } else {
      alert(`FAST VERIFY: ${(data.fast.match_ratio * 100).toFixed(1)}%`);
    }
  };

  return (
    <button onClick={runVerify}>
      🔍 Verify Flash
    </button>
  );
}
    alert(`
🔍 VERIFY RESULT

ISO: ${data.iso_hash.slice(0, 12)}...
USB: ${data.usb_hash.slice(0, 12)}...

${data.match ? "✅ MATCH (SAFE)" : "❌ MISMATCH (CORRUPTED)"}
`);
  };

  return (
    <button onClick={runVerify}>
      🔍 Verify Flash
    </button>
  );
}
