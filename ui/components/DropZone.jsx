import { useState } from "react";

export default function DropZone({ onDropISO }) {
  const [dragging, setDragging] = useState(false);

  const handleDrop = (e) => {
    e.preventDefault();
    setDragging(false);

    const files = Array.from(e.dataTransfer.files);
    const isos = files.filter(f => f.name.endsWith(".iso"));

    onDropISO(isos);
  };

  return (
    <div
      onDragOver={(e) => { e.preventDefault(); setDragging(true); }}
      onDragLeave={() => setDragging(false)}
      onDrop={handleDrop}
      style={{
        border: "2px dashed #0a84ff",
        borderRadius: 20,
        padding: 40,
        textAlign: "center",
        background: dragging ? "rgba(10,132,255,0.2)" : "transparent"
      }}
    >
      <h2>📦 Drag & Drop ISO Here</h2>
      <p>Drop Windows / Linux ISO to add to USB</p>
    </div>
  );
}
