def calc_money(name2ref,name2money,name,amount):
    money=amount*100 #칫솔 판 금액
    while name!="-" and money!=0: #root 노드가 아니며 할당된 금액이 0보다 클 때
        ref_fee=int(money*0.1) #추천 수수료 계산
        name2money[name]+=money-ref_fee #해당 name 사원에게 수수료 제한 금액 할당
        name=name2ref[name] #추천인으로 차례를 넘겨줌
        money=ref_fee #추천인은 공제되지 않은 수수료를 base money로 갖는다 

def solution(enroll, referral, seller, amount):
    name2ref={name:ref for (name,ref) in zip(enroll,referral)} #이름으로 추천인 찾는 dict
    name2money={name: 0 for name in enroll} #이름으로 금액 가져오는 dict
    
    for name,cnt in zip(seller,amount):
        calc_money(name2ref,name2money,name,cnt)
    
    return list(name2money.values())