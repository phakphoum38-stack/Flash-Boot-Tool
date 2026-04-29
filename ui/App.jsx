import DropZone from "./components/DropZone";
import Verify from "./components/Verify";

export default function App() {
  const handleDropISO = async (isos) => {
    const form = {
      device: "/dev/sdb",
      isos: isos.map(i => i.path)
    };

    await window.__TAURI__.invoke("ventoy_add_iso", form);
  };

  return (
    <div style={{ padding: 30 }}>
      <h1>⚡ FlashForge Ventoy Mode</h1>

      <DropZone onDropISO={handleDropISO} />

      <button onClick={() =>
        window.__TAURI__.invoke("ventoy_install", { device: "/dev/sdb" })
      }>
        Install Ventoy Bootloader
      </button>
    </div>
  );
}

function App() {

  const iso = "/path/to/windows.iso";
  const device = "/dev/sdb";

  return (
    <div>
      <h1>Flash Tool</h1>

      {/* ปุ่ม verify */}
      <Verify iso={iso} device={device} />

    </div>
  );
}

export default App;
