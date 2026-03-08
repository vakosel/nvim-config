#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Terminal Calendar Utility

Requirements:
- Python 3
- dateparser (pip install dateparser)

Usage Examples:
    python3 terminal_calendar.py 2023-08-14 --three --weeknumbers --file highlights.txt --format %Y-%m-%d
"""

import argparse
import os
import re
import sys
from calendar import TextCalendar
from datetime import datetime, timedelta

import dateparser

# Terminal color codes
META = '\33[90m'
TODAY = '\33[7m'
WEEKEND = '\33[36m'
CEND = '\33[0m'

def color(text, color_code):
    """Applies terminal color if output is a tty."""
    return color_code + text + CEND if sys.stdout.isatty() else text

def formatmonth(cal, date, highlight, current=False, weeknumbers=False, w=0):
    """Return formatted month as lines (strings)."""
    theyear = date.year
    themonth = date.month
    firstweeknumber = date.replace(day=1).isocalendar()[1] if weeknumbers else -100
    weekcolumn = ' № ' if weeknumbers else ''
    weekpadding = 3 if weeknumbers else 0
    day = date.day if current else 0
    highlightdays = [x.day for x in highlight if x.year == theyear and x.month == themonth]
    w = max(2, w)
    s = []
    s.append(color(cal.formatmonthname(theyear, themonth, 7 * (w + 1) + weekpadding - 1), META))
    s.append(color(cal.formatweekheader(w).rstrip() + weekcolumn, META))
    for i, week in enumerate(cal.monthdays2calendar(theyear, themonth)):
        s.append(formatweek(week, highlightdays, firstweeknumber + i, day, w).rstrip())
    return s

def formatweek(theweek, highlightdays, weeknumber, day, width):
    weekcolumn = color(" %i" % weeknumber, META) if weeknumber > 0 else ''
    return ' '.join(formatday(highlightdays, d, wd, day, width) for (d, wd) in theweek) + weekcolumn

def formatday(highlightdays, day, weekday, today, width):
    if day == 0:
        s = ''
    elif day == today:
        s = color('%2i' % day, TODAY)
    elif day in highlightdays or weekday > 4:
        s = color('%2i' % day, WEEKEND)
    else:
        s = '%2i' % day
    return s.center(width)

def align(lines, pos, length):
    """Aligns calendar columns, stripping ANSI color codes for width calculation."""
    text = "" if len(lines) <= pos else lines[pos]
    printable = re.sub(r"\33\[[0-9;]*m", "", text)
    text += " " * (length - len(printable))
    return text

def load_highlight_dates(filename, dateformat):
    """Loads and parses highlight dates from a file."""
    highlight = []
    try:
        with open(filename, 'r') as myfile:
            for line in myfile:
                line = line.strip()
                if not line:
                    continue
                try:
                    highlight.append(datetime.strptime(line, dateformat))
                except ValueError:
                    print(f"Warning: Could not parse date '{line}' with format '{dateformat}'", file=sys.stderr)
    except Exception as e:
        print(f"Error reading highlight file: {e}", file=sys.stderr)
    return highlight

def parse_target_date(args):
    """Parses the target date from args or uses today."""
    if not args.date or len(args.date) == 0:
        return datetime.today()
    s = ' '.join(args.date)
    parsed = dateparser.parse(s, settings={'PREFER_DAY_OF_MONTH': 'first'})
    if not parsed:
        print(f"Could not interpret date '{s}', defaulting to today.", file=sys.stderr)
        return datetime.today()
    return parsed

def main():
    parser = argparse.ArgumentParser(description='Nicer Calendar for your terminal')
    parser.add_argument('date', nargs="*", default=None, help='Human readable date')
    parser.add_argument('-3', '--three',  action='store_true', help='Display three months spanning the date.')
    parser.add_argument('-w', '--weeknumbers', action='store_true', help='Display week numbers in the calendar')
    parser.add_argument('-s', '--sunday', action='store_true', help='Display Sunday as the first day of the week')
    parser.add_argument('-f', '--file', help='File with dates to highlight')
    parser.add_argument('-d', '--format', default='%Y-%m-%d', help='Format of date in file')
    parser.add_argument('-y', '--year', type=int, help='Display calendar for a whole year')
    args = parser.parse_args()

    firstweekday = 6 if args.sunday else 0
    cal = TextCalendar(firstweekday)
    highlight = load_highlight_dates(args.file, args.format) if args.file else []
    today = parse_target_date(args)

    this_month = formatmonth(cal, today, highlight, current=True, weeknumbers=args.weeknumbers)

    if not args.three:
        print("\n".join(this_month))
    else:
        # Calculate column width dynamically (hardcoded fallback if terminal size is unknown)
        try:
            columns = os.get_terminal_size().columns
        except OSError:
            columns = 80
        l = 24 if args.weeknumbers else 21

        prev_month_date = today.replace(day=1) - timedelta(days=1)
        next_month_date = today.replace(day=1) + timedelta(days=31)

        prev_month = formatmonth(cal, prev_month_date, highlight, weeknumbers=args.weeknumbers)
        next_month = formatmonth(cal, next_month_date, highlight, weeknumbers=args.weeknumbers)
        rows = max(len(prev_month), len(this_month), len(next_month))

        if l*2 >= columns:
            print("\n".join(prev_month))
            print("\n" + "\n".join(this_month))
            print("\n" + "\n".join(next_month))
        elif l*3 >= columns:
            for i in range(rows):
                print(align(prev_month, i, l), align(this_month, i, l))
            print("\n" + "\n".join(next_month))
        else:
            for i in range(rows):
                print(align(prev_month, i, l), align(this_month, i, l), align(next_month, i, l))
    if args.year:
        for month in range(1, 13):
            date_obj = datetime(args.year, month, 1)
            month_lines = formatmonth(cal, date_obj, highlight, weeknumbers=args.weeknumbers)
            print("\n".join(month_lines))
            print()  # Empty line after each month
        return
if __name__ == "__main__":
    main()


