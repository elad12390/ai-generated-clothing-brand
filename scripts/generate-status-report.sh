#!/bin/bash
# Script to generate a status report template

# Get current date information
CURRENT_DATE=$(date)
WEEK_NUMBER=$(date +%V)
START_DATE=$(date -d 'monday' +%Y-%m-%d)
END_DATE=$(date -d 'friday' +%Y-%m-%d)

# Create status report file
STATUS_REPORT_FILE="docs/tasks/status-report-week-$WEEK_NUMBER.md"

# Copy template and replace placeholders
sed -e "s/{week_number}/$WEEK_NUMBER/g" \
    -e "s/{start_date}/$START_DATE/g" \
    -e "s/{end_date}/$END_DATE/g" \
    -e "s/{percentage}/0/g" \
    docs/tasks/status-report-template.md > $STATUS_REPORT_FILE

echo "Status report template generated: $STATUS_REPORT_FILE"
echo "Please update the template with actual progress information."