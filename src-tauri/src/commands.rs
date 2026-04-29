use std::process::Command;

#[tauri::command]
pub fn flash_dd(iso: String, device: String) -> String {
    let output = Command::new("dd")
        .args([
            &format!("if={}", iso),
            &format!("of={}", device),
            "bs=4M",
            "status=progress"
        ])
        .output();

    match output {
        Ok(_) => "Flash completed".to_string(),
        Err(e) => format!("Error: {}", e),
    }
}

#[tauri::command]
pub fn ventoy_install(device: String) -> String {
    let output = Command::new("sh")
        .arg("-c")
        .arg(format!("ventoy -i {}", device))
        .output();

    match output {
        Ok(_) => "Ventoy installed".to_string(),
        Err(e) => e.to_string()
    }
}

#[tauri::command]
pub fn ventoy_add_iso(device: String, isos: Vec<String>) -> String {
    for iso in isos {
        Command::new("cp")
            .arg(&iso)
            .arg(format!("{}/ISO/", device))
            .output()
            .ok();
    }

    "ISOs added to Ventoy USB".to_string()
}

#[tauri::command]
pub fn auto_fix(iso: String, usb: String, qemu_result: String) -> String {

    let output = std::process::Command::new("python3")
        .args([
            "engine/auto_fix_engine.py",
            &iso,
            &usb,
            &qemu_result
        ])
        .output();

    match output {
        Ok(o) => String::from_utf8_lossy(&o.stdout).to_string(),
        Err(e) => e.to_string()
    }
}
