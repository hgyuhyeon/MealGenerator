# USE mySQL

SET foreign_key_checks = 0;
DROP table IF EXISTS foodata;
DROP table IF EXISTS material;
SET foreign_key_checks = 1;

CREATE table foodata (
	category char(4), # 기존의 rice,soup,sd1,sd2,sd3,sd4,kimchi,dessert를 밥, 국, 반찬, 김치, 디저트로 나눔
    fname char(30), #음식의 이름
    kcal int #칼로리
) ENGINE = InnoDB;

CREATE table material (
	category char(10), #분류
	mname char(30), #이름
    kcal int, #칼로리
    chydrate int, #탄수화물 함량
    protein int, #단백질 함량
    fat int #지방 함량
) ENGINE = InnoDB;



#DB출처: https://m.blog.naver.com/PostView.nhn?blogId=yoous2923&logNo=220702822750&proxyReferer=http:%2F%2Fwww.google.com%2Furl%3Fsa%3Dt%26rct%3Dj%26q%3D%26esrc%3Ds%26source%3Dweb%26cd%3D%26ved%3D2ahUKEwjZkJLg9s7pAhVSVN4KHWRVAakQFjAQegQIAhAB%26url%3Dhttp%253A%252F%252Fm.blog.naver.com%252Fyoous2923%252F220702822750%26usg%3DAOvVaw34NPzZZmR8dxBfes2bcALx
#모든 음식은 1인분, 1개, 1포장 기준
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

INSERT INTO material(category, mname, kcal, chydrate, protein, fat)
	VALUES('스프','쇠고기스프','25','0','0','0');
INSERT INTO material(category, mname, kcal, chydrate, protein, fat)
	VALUES('스프','쇠고기야채스프','50','25','0','25');
INSERT INTO material(category, mname, kcal, chydrate, protein, fat)
	VALUES('스프','양송이크림스프','75','25','0','25');
INSERT INTO material(category, mname, kcal, chydrate, protein, fat)
	VALUES('스프','크림스프','50','25','0','25');
    
INSERT INTO material(category, mname, kcal, chydrate, protein, fat)
	VALUES('양정식','돈까스정식','500','175','100','225');
INSERT INTO material(category, mname, kcal, chydrate, protein, fat)
	VALUES('양정식','비후가스정식','450','175','100','175');
INSERT INTO material(category, mname, kcal, chydrate, protein, fat)
	VALUES('양정식','생선까스정식','300','125','50','125');
INSERT INTO material(category, mname, kcal, chydrate, protein, fat)
	VALUES('양정식','안심스테이크정식','650','250','150','250');
INSERT INTO material(category, mname, kcal, chydrate, protein, fat)
	VALUES('양정식','함박스테이크정식','575','175','125','300');
    
INSERT INTO material(category, mname, kcal, chydrate, protein, fat)
	VALUES('과일','바나나','100','100','0','0');
    
INSERT INTO material(category, mname, kcal, chydrate, protein, fat)
	VALUES('과일통조림','복숭아통조림(백도)','275','275','0','0');
INSERT INTO material(category, mname, kcal, chydrate, protein, fat)
	VALUES('과일통조림','','','','','');
    
INSERT INTO material(category, mname, kcal, chydrate, protein, fat)
	VALUES('쨈','딸기쨈','50','50','0','0');
INSERT INTO material(category, mname, kcal, chydrate, protein, fat)
	VALUES('쨈','사과쨈','50','50','0','0');
INSERT INTO material(category, mname, kcal, chydrate, protein, fat)
	VALUES('쨈','포도쨈','50','50','0','0');

INSERT INTO material(category, mname, kcal, chydrate, protein, fat)
	VALUES('견과류','','','','','');

INSERT INTO material(category, mname, kcal, chydrate, protein, fat)
	VALUES('빵','','','','','');
    
INSERT INTO material(category, mname, kcal, chydrate, protein, fat)
	VALUES('과자류','','','','','');
    
INSERT INTO material(category, mname, kcal, chydrate, protein, fat)
	VALUES('생야채','','','','','');

INSERT INTO material(category, mname, kcal, chydrate, protein, fat)
	VALUES('유제품','','','','','');
    
INSERT INTO material(category, mname, kcal, chydrate, protein, fat)
	VALUES('음료','','','','','');
    
INSERT INTO material(category, mname, kcal, chydrate, protein, fat)
	VALUES('차','','','','','');
    
INSERT INTO material(category, mname, kcal, chydrate, protein, fat)
	VALUES('주류','','','','','');
    
INSERT INTO material(category, mname, kcal, chydrate, protein, fat)
	VALUES('시리얼','아몬드후레이크','375','275','25','50');
INSERT INTO material(category, mname, kcal, chydrate, protein, fat)
	VALUES('시리얼','콘푸로스트','350','325','25','0');
    
INSERT INTO material(category, mname, kcal, chydrate, protein, fat)
	VALUES('조미료','','','','','');
    
INSERT INTO material(category, mname, kcal, chydrate, protein, fat)
	VALUES('떡','','','','','');
    
INSERT INTO material(category, mname, kcal, chydrate, protein, fat)
	VALUES('어육가공품','','','','','');
    
    
    
INSERT INTO material(category, mname, kcal, chydrate, protein, fat)
	VALUES('','','','','','');
    
    
SELECT * from material
