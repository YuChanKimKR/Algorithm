#!/bin/bash

# 시작 날짜 설정 (2023년 첫 번째 주 일요일)
start_date="2023-01-01"

# 도트맵 정의
dotmap=(
  "01110 11111  0000   11111   11111  "
  "01010 10001  0000   10001   10001  "
  "01010 11111  0000   11111   11111  "
  "01010 10001  0000   10000   10000  "
  "01110 10001  0000   11111   11111  "
  "01110 11111  11111  11111   11111  "
  "01110 11111  11111  10001   11111  "
  "01110 11111  11111  11111   01110  "
)

# 리포지토리 경로 설정
repo_path="C:/Users/dbcks/Algorithm"  # 본인의 Git 리포지토리 경로
cd "$repo_path"

# 도트맵에 따라 커밋 생성
for row in "${!dotmap[@]}"; do
  line="${dotmap[$row]}"
  for ((col=0; col<${#line}; col++)); do
    if [[ "${line:$col:1}" == "1" ]]; then
      # 날짜 계산
      commit_date=$(date -d "$start_date +$((col * 7 + row)) days" +%Y-%m-%d)
      # 커밋 생성
      for i in {1..5}; do  # 강도를 높이기 위해 반복
        echo "dbcks357 on $commit_date" > file.txt
        git add file.txt
        GIT_COMMITTER_DATE="$commit_date 12:00:00" GIT_AUTHOR_DATE="$commit_date 12:00:00" git commit -m "dbcks357"
      done
    fi
  done
done

# 원격으로 푸시
git push origin main
