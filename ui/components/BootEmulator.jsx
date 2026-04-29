export default function BootEmulator({ iso }) {

  const run = async () => {
    const res = await window.__TAURI__.invoke("emulate_boot", {
      iso
    });

    alert(`
🧪 BOOT EMULATOR RESULT

Boot Success: ${res.result.boot_success}
Mode: ${res.result.mode}
Error: ${res.result.error || "none"}
`);
  };

  return (
    <button onClick={run}>
      🧪 Real Boot Emulator (QEMU)
    </button>
  );
}
