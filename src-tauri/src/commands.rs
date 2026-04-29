#[tauri::command]
pub fn emulate_boot(iso: String) -> String {

    let output = std::process::Command::new("python3")
        .args(["engine/qemu_boot_emulator.py", &iso])
        .output();

    match output {
        Ok(o) => String::from_utf8_lossy(&o.stdout).to_string(),
        Err(e) => e.to_string()
    }
}
