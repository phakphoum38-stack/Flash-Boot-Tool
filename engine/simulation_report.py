def format_report(sim):
    return f"""
🧪 BOOT SIMULATION REPORT
------------------------
ISO: {sim['iso']}
Type: {sim['type']}

Bootable: {'YES' if sim['bootable'] else 'NO'}
Risk Level: {sim['risk']}

Issues:
- {'No issues' if not sim['issues'] else '\n- '.join(sim['issues'])}

Fix Suggestions:
- {'None' if not sim['fix_suggestion'] else '\n- '.join(sim['fix_suggestion'])}
"""
