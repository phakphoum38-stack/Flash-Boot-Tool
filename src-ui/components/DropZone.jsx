import React from "react";

export default function DropZone({ setIso }) {
  const onDrop = (e) => {
    e.preventDefault();
    const file = e.dataTransfer.files[0];
    if (file) {
      setIso(file.path || file.name); // Tauri/Electron จะได้ path จริง
    }
  };

  return (
    <div
      onDragOver={(e) => e.preventDefault()}
      onDrop={onDrop}
      style={{
        border: "2px dashed #aaa",
        padding: 40,
        textAlign: "center",
        borderRadius: 20
      }}
    >
      📂 Drag & Drop ISO here
    </div>
  );
}
