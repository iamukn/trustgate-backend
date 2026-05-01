from datetime import datetime, timezone

def get_days_since_swap(swap_time_str):
    swap_time = datetime.fromisoformat(swap_time_str.replace("Z", "+00:00"))
    now = datetime.now(timezone.utc)

    diff = now - swap_time
    return round(diff.total_seconds() / 86400, 0)  # days
