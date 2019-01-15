# PagerDitty

Simple script I threw together to generate oncall waiting and working time reports for my team of SREs.

## Installation

Python 2

    pip install -r requirements.txt
    python setup.py install

Python 3

    pip3 install -r requirements.txt
    python3 setup.py install

## Usage

    generate_report.py [-h] --pd_id PD_ID --pd_api_key PD_API_KEY
                            --pd_schedule_id PD_SCHEDULE_ID
                            [--slack_username SLACK_USERNAME] --start START
                            [--durationunits {days,months,years}]
                            [--duration DURATION] [--tz TZ]
                            [--workdays {MonFri,SunThu}]
                            [--day_start_hour DAY_START_HOUR]
                            [--day_start_min DAY_START_MIN]
                            [--day_length_hours DAY_LENGTH_HOURS]

    Generate Pagerduty oncall waiting and working time reports.

    optional arguments:
    -h, --help            show this help message and exit
    --pd_id PD_ID         PagerDuty User ID, e.g. ABCDEFG
    --pd_api_key PD_API_KEY
                            PagerDuty API key
    --pd_schedule_id PD_SCHEDULE_ID
                            PagerDuty schedule ID(s), e.g. DEFGHIJ
    --slack_username SLACK_USERNAME
                            Slack username to use when determining incident
                            engagement
    --start START         Start of the report period
    --durationunits {days,months,years}
                            Unit of measure for the --duration argument
    --duration DURATION   Report duration from start in --durationunits
    --tz TZ               Time zone parseable by the datetime.tz library
    --workdays {MonFri,SunThu}
                            Days which are considered workdays
    --day_start_hour DAY_START_HOUR
                            Working shift start time hour
    --day_start_min DAY_START_MIN
                            Working shift start time, minutes after the
                            --day_start_hour
    --day_length_hours DAY_LENGTH_HOURS
                            Duration of a working shift, in hours
