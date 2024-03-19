def solution(players, callings):
    # 플레이어와 인덱스의 딕셔너리 생성
    player_index_map = {player: index for index, player in enumerate(players)}
    
    for calling in callings:
        # 호출된 플레이어의 인덱스 가져오기
        player_index = player_index_map[calling]
        
        # 인덱스를 기반으로 인접한 두 플레이어 선택
        prev_player, cur_player = players[player_index - 1], players[player_index]
        
        # 플레이어 위치 교환
        players[player_index - 1], players[player_index] = cur_player, prev_player
        
        # 딕셔너리 업데이트
        player_index_map[prev_player], player_index_map[cur_player] = player_index, player_index - 1
        
    return players
