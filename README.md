# grouping-members-to-slack
pick some members to do somthing from members then send to slack

# 자세한 설정 방법은 아래 링크를 참고해주세요.
https://velog.io/@ja2ykweon/%EB%9E%9C%EB%8D%A4-%EC%B2%AD%EC%86%8C-%EB%8B%B9%EB%B2%88-%EC%8A%AC%EB%9E%99-%EC%9E%90%EB%8F%99-%EC%95%8C%EB%A6%BC-with-aws-lambda-13

# 원본은 1명을 선택하지만, 여러 명을 선택할 수 있게 하였습니다.

# 환경변수는 아래와 같습니다.
1. SLACK_TOKEN
2. MEMBERS
3. SLACK_CHANNEL
4. (추가 내용)GROUP_SIZE: 원본과 달리 복수의 멤버를 sub-set으로 뽑을 수 있습니다.
