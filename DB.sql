# USE mySQL

SET foreign_key_checks = 0;
DROP table IF EXISTS foodata;
SET foreign_key_checks = 1;

CREATE table foodata (
	category char(4), # 기존의 rice,soup,sd1,sd2,sd3,sd4,kimchi,dessert를 밥, 국, 반찬, 김치, 디저트로 나눔
    fname char(30), #음식의 이름
    kcal int #칼로리
) ENGINE = InnoDB;

INSERT INTO foodata(category, fname, kcal)
	VALUES('밥','흰쌀밥','300');
INSERT INTO foodata(category, fname, kcal)
	VALUES('국','배추된장국','200');
INSERT INTO foodata(category, fname, kcal)
	VALUES('반찬','매콤돈갈비찜','352');
INSERT INTO foodata(category, fname, kcal)
	VALUES('반찬','도토리묵야채무침','220');
INSERT INTO foodata(category, fname, kcal)
	VALUES('김치','배추김치','50');
INSERT INTO foodata(category, fname, kcal)
	VALUES('디저트','자몽에이드','70');

SELECT * from foodata
#참고: 별빛식당 20200525 ~ 20200529 가격: 5300원(조합원 4900원)
#INSERT INTO category (rice, soup, sd1, sd2, sd3, sd4, kimchi, dessert, kcal) 
#	VALUES('흰쌀밥', '어묵무국','파채불고기','오징어야채무침','야채계란찜',' ','배추김치','자두쿨피스','-1');
#INSERT INTO category (rice, soup, sd1, sd2, sd3, sd4, kimchi, dessert, kcal) 
#	VALUES('흰쌀밥', '계란파국','깐풍기','순대야채볶음','양상추샐러드/화이트소스',' ','배추김치','요구르트','-1');
#INSERT INTO category (rice, soup, sd1, sd2, sd3, sd4, kimchi, dessert, kcal) 
#	VALUES('흰쌀밥', '두부호박된장국','제육볶음','단호박&만두튀김/초간장','닭가슴살겨자채',' ','배추김치','복숭아쿨피스','-1');
#INSERT INTO category (rice, soup, sd1, sd2, sd3, sd4, kimchi, dessert, kcal) 
#	VALUES('흰쌀밥', '옥수수스프','찜닭','미트볼토마토스파게티','수제오이무피클',' ','배추김치','망고주스','-1');
 
 #참고: 은하수식당 20200525~20200529 가격: 6000원(조합원 5000원)
#INSERT INTO category (rice, soup, sd1, sd2, sd3, sd4, kimchi, dessert, kcal) 
#	VALUES('찰수수밥', '팽이무국','소고기불고기','치커리샐러드&유자청소스','우엉채튀김','콩나물무침','포기김치','바나나','-1');
#INSERT INTO category (rice, soup, sd1, sd2, sd3, sd4, kimchi, dessert, kcal) 
#	VALUES('차조밥', '미역국','큐브스테이크','숙주부추무침/깨소스','셀러리피클','무생채','포기김치','무생채','-1');
#INSERT INTO category (rice, soup, sd1, sd2, sd3, sd4, kimchi, dessert, kcal) 
#	VALUES('보리밥', '계란파국','옛날닭튀김&칠리소스','쑥갓두부무침','무들깨가루볶음','부들어묵볶음','포기김치','바나나','-1');
#INSERT INTO category (rice, soup, sd1, sd2, sd3, sd4, kimchi, dessert, kcal) 
#	VALUES('비빔밥&고추장소스', '유부미소된장국',' ','포실포실찐감자','양상추샐러드&화이트소스',' ','열무김치','오렌지','-1');
#INSERT INTO category (rice, soup, sd1, sd2, sd3, sd4, kimchi, dessert, kcal) 
#	VALUES('검정쌀밥', '콩나물국','삼치무조림','애배추겉절이','상하이스파게티','고추장멸치볶음','포기김치','오렌지','-1');
 
