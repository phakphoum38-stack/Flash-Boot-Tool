export default function AutoFix({ iso, usb, qemuResult }) {

  const runFix = async () => {
    const res = await fetch("http://localhost:8000/auto-fix", {
      method: "POST",
      headers: {"Content-Type":"application/json"},
      body: JSON.stringify({
        iso,
        usb,
        qemu_result: qemuResult
      })
    });

    const data = await res.json();

    alert(`
🔧 AUTO FIX COMPLETE

Strategies:
${data.strategies.join("\n")}

Actions:
${data.actions.join("\n")}
`);
  };

  return (
    <button onClick={runFix}>
      🔧 Auto Fix Boot (AI)
    </button>
  );
}
