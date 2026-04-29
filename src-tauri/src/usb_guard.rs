pub fn is_safe_device(device: &str) -> bool {
    let blocked = vec![
        "/dev/sda", "/dev/nvme0n1",
        "C:", "D:" // Windows (กันพลาดเบื้องต้น)
    ];

    !blocked.iter().any(|d| device.starts_with(d))
}
