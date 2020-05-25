#스토리보드에 맞춰 수정한 DB의 구성

CREATE table foodata (
	category char(4), # 기존의 rice,soup,sd1,sd2,sd3,sd4,kimchi,dessert를 밥, 국, 반찬, 김치, 디저트로 나눔
    fname char(30), #음식의 이름
    kcal int, #칼로리
    chdrate int, #탄수화물 함량
    protein int, #단백질 함량
    fat int, #지방 함량
    sodium int, #나트륨 함량
    potsium int  #칼륨 함량
) ENGINE = InnoDB;
