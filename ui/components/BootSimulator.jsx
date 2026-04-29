export default function BootSimulator({ iso }) {

  const runSim = async () => {
    const res = await window.__TAURI__.invoke("simulate_boot", {
      iso
    });

    alert(res.report);
  };

  return (
    <div>
      <button onClick={runSim}>
        🧪 Boot Simulator
      </button>
    </div>
  );
}
