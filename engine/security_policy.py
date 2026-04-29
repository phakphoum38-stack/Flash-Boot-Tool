SAFE_STRATEGIES = {
    "install_efi",
    "rebuild_grub",
    "split_wim",
    "rebuild_mbr"
}

def filter_strategies(strategies):
    return [s for s in strategies if s in SAFE_STRATEGIES]
