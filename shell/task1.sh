#!/bin/bash

# Task 1: system_health_check.sh

LOG_DATE=$(date +"%Y-%m-%d")
PROCESS_LOG="process_log_${LOG_DATE}.log"
ps aux > "$PROCESS_LOG"
echo "Running processes saved to $PROCESS_LOG"

# 2. High Memory Usage Check
HIGH_MEM_LOG="high_mem_processes.log"

# Portable approach: no --sort
HIGH_MEM_PROCESSES=$(ps aux | awk '$4+0 > 30')

if [[ -n "$HIGH_MEM_PROCESSES" ]]; then
    echo "WARNING: Processes using more than 30% memory detected!"
    echo "High memory usage processes on $LOG_DATE:" >> "$HIGH_MEM_LOG"
    echo "$HIGH_MEM_PROCESSES" >> "$HIGH_MEM_LOG"
    echo "" >> "$HIGH_MEM_LOG"
fi

# 3. Disk Space Check (Portable and Accurate)
DISK_USAGE=$(df -P / | awk 'NR==2 {gsub(/%/, "", $5); print $5}')

if [[ $DISK_USAGE -gt 80 ]]; then
    echo "WARNING: Disk usage on / is above 80% (Current: ${DISK_USAGE}%)"
fi

# 4. Summary
TOTAL_PROCESSES=$(ps aux | wc -l)
HIGH_MEM_COUNT=$(echo "$HIGH_MEM_PROCESSES" | grep -c '.')

echo ""
echo "===== SYSTEM HEALTH SUMMARY ====="
echo "Total running processes          : $TOTAL_PROCESSES"
echo "Processes using >30% memory      : $HIGH_MEM_COUNT"
echo "Disk usage on /                  : ${DISK_USAGE}%"
echo "=================================="
