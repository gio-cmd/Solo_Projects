import math

def make_readable(seconds):
    if seconds < 60:
        if seconds == 0:
            return "00:00:00"
        return f"00:00:{seconds:02d}"
    elif seconds >= 60 and seconds < 3600:
        if seconds % 60 == 0:
            if len(str(seconds // 60)) == 1:
                return f"00:0{seconds // 60}:{seconds % 60:02d}"
            return f"00:{seconds // 60:02d}:00"
        elif len(str(seconds // 60)) == 1:
            return f"00:0{seconds // 60}:{seconds % 60:02d}"
        return f"00:{seconds // 60:02d}:{seconds % 60:02d}"
    else:
        hours = seconds // 3600
        minutes = (seconds - (hours * 3600)) // 60
        second = (seconds - (hours * 3600)) % 60
        if seconds % 3600 == 0:
            if len(str(seconds // 3600)) == 1:
                return f"0{seconds // 3600}:00:00"
            return f"{seconds // 3600}:00:00"
        elif seconds % 3600 != 0:
            if len(str(second)) == 1:
                return f"{hours}:{minutes:02d}:0{second}"
            elif len(str(hours)) == 1:
                if len(str(minutes)) == 1:
                    if len(str(second)) == 1:
                        return f"0{hours}:0{minutes}:0{second}"
                    return f"0{hours}:0{minutes}:{second}"
                elif len(str(second)) == 1:
                    return f"0{hours}:{minutes}:0{second}"
                return f"0{hours}:{minutes}:{second}"
            elif len(str(minutes)) == 1:
                if len(str(second)) == 1:
                    return f"{hours}:0{minutes}:0{second}"
                return f"{hours}:0{minutes}:{second}"
            return f"{hours}:{minutes}:{second}"
        
print(make_readable(6231))


