export default function AIFix({ iso, usb }) {

  const run = async () => {
    const res = await fetch("http://localhost:8000/ai-auto-fix", {
      method: "POST",
      headers: {"Content-Type":"application/json"},
      body: JSON.stringify({ iso, usb })
    });

    const data = await res.json();

    alert(`
🧠 AI AUTO FIX

Signature: ${data.signature}
Source: ${data.ai_source}

Boot Success: ${data.recheck.boot_success}
`);
  };

  return (
    <button onClick={run}>
      🧠 Smart AI Fix (Self-learning)
    </button>
  );
}
