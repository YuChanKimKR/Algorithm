#!/bin/bash

# 시작 날짜 설정 (2023년 첫 번째 주 일요일)
start_date="2023-01-01"

# 도트맵 정의 (7x52 그리드)
dotmap=(
  "1110001111100111100000000111111111110" # d
  "1010001000100100100000000100001000100" # b
  "1010001111100111100000000111111111110" # c
  "1010001000100100000000000100000000100" # k
  "1110001000100100000000000111111111110" # s
  "1111101111101111101111100000000000000" # 3
  "1111101111101111101111100000000000000" # 5
  "1111101111101111101111100000000000000" # 7
)

# 리포지토리 경로 설정
repo_path="C:/Users/dbcks/Algorithm" # 본인의 Git 리포지토리 경로
cd "$repo_path"

# 도트맵에 따라 커밋 생성
for row in "${!dotmap[@]}"; do
  line="${dotmap[$row]}"
  for ((col=0; col<${#line}; col++)); do
    if [[ "${line:$col:1}" == "1" ]]; then
      # 날짜 계산 (start_date + week * col + day * row)
      commit_date=$(date -d "$start_date +$((col * 7 + row)) days" +%Y-%m-%d)
      # 커밋 생성
      for i in {1..5}; do # 원하는 커밋 강도 (5번 반복)
        echo "dbcks357 on $commit_date" > file.txt
        git add file.txt
        GIT_COMMITTER_DATE="$commit_date 12:00:00" GIT_AUTHOR_DATE="$commit_date 12:00:00" git commit -m "dbcks357"
      done
    fi
  done
done

# 원격으로 푸시
git push origin main
