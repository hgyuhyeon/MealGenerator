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
    kcal float, #칼로리
    chydrate float, #탄수화물 함량
    protein float, #단백질 함량
    fat float #지방 함량
) ENGINE = InnoDB;



#DB출처: https://m.blog.naver.com/PostView.nhn?blogId=yoous2923&logNo=220702822750&proxyReferer=http:%2F%2Fwww.google.com%2Furl%3Fsa%3Dt%26rct%3Dj%26q%3D%26esrc%3Ds%26source%3Dweb%26cd%3D%26ved%3D2ahUKEwjZkJLg9s7pAhVSVN4KHWRVAakQFjAQegQIAhAB%26url%3Dhttp%253A%252F%252Fm.blog.naver.com%252Fyoous2923%252F220702822750%26usg%3DAOvVaw34NPzZZmR8dxBfes2bcALx
#모든 음식은 1인분, 1개, 1포장 기준
INSERT INTO foodata(category, fname, kcal)
	VALUES
    ('밥','흰쌀밥','300'),
    ('국','배추된장국','200'),
	('반찬','매콤돈갈비찜','352'),
	('반찬','도토리묵야채무침','220'),
	('김치','배추김치','50'),
	('디저트','자몽에이드','70');

INSERT INTO material(category, mname, kcal, chydrate, protein, fat)
	VALUES
    ('스프','쇠고기스프','25','0','0','0'),
	('스프','쇠고기야채스프','50','25','0','25'),
	('스프','양송이크림스프','75','25','0','25'),
	('스프','크림스프','50','25','0','25');
    
INSERT INTO material(category, mname, kcal, chydrate, protein, fat)
	VALUES
    ('양정식','돈까스정식','500','175','100','225'),
	('양정식','비후가스정식','450','175','100','175'),
	('양정식','생선까스정식','300','125','50','125'),
	('양정식','안심스테이크정식','650','250','150','250'),
	('양정식','함박스테이크정식','575','175','125','300');
    
INSERT INTO material(category, mname, kcal, chydrate, protein, fat)
	VALUES
    ('과일','키위','50','50','0','0'),
	('과일','토마토','25','25','0','0'),
    ('과일','파인애플','400','400','0','0'),
    ('과일','포도','175','175','0','0'),
    ('과일','감','75','75','0','0'),
    ('과일','건포도','1.5','1.5','0','0'),
    ('과일','곶감','75','75','0','0'),
    ('과일','귤','50','50','0','0'),
    ('과일','대추','5','5','0','0'),
    ('과일','딸기','7','7','0','0'),
    ('과일','멜론(1조각)','50','50','0','0'),
    ('과일','바나나','100','100','0','0'),
	('과일','방울토마토','4.5','4.5','0','0'),
    ('과일','배','150','150','0','0'),
    ('과일','복숭아(백도)','100','100','0','0'),
    ('과일','복숭아(황도)','75','75','0','0'),
    ('과일','사과','175','175','0','0'),
    ('과일','수박','37.5','37.5','0','0'),
    ('과일','오렌지','75','75','0','0'),
    ('과일','자두','25','25','0','0'),
    ('과일','자몽','100','100','0','0'),
    ('과일','참외','125','125','0','0');

INSERT INTO material(category, mname, kcal, chydrate, protein, fat)
	VALUES
    ('과일통조림','복숭아통조림(백도)','275','275','0','0'),
	('과일통조림','복숭아통조림(황도)','225','225','0','0'),
	('과일통조림','파인애플통조림','525','500','25','0'),
	('과일통조림','파인애플통조림(1조각)','75','75','0','0');

INSERT INTO material(category, mname, kcal, chydrate, protein, fat)
	VALUES
    ('쨈','딸기쨈','50','50','0','0'),
	('쨈','사과쨈','50','50','0','0'),
	('쨈','포도쨈','50','50','0','0');

INSERT INTO material(category, mname, kcal, chydrate, protein, fat)
	VALUES
    ('견과류','군밤','50','50','0','0'),
	('견과류','땅콩','75','0','25','50'),
    ('견과류','아몬드','75','0','0','75'),
    ('견과류','은행','25','25','0','0'),
    ('견과류','잣','100','0','25','75'),
    ('견과류','호두','75','0','0','75');

INSERT INTO material(category, mname, kcal, chydrate, protein, fat)
	VALUES('빵','','','','','');
    
INSERT INTO material(category, mname, kcal, chydrate, protein, fat)
	VALUES('과자류','','','','','');
    
INSERT INTO material(category, mname, kcal, chydrate, protein, fat)
	VALUES
    ('생야채','깻잎','0','0','0','0'),
	('생야채','당근','75','75','0','0'),
	('생야채','두부(1/6모)','75','0','25','50'),
	('생야채','상추','25','0','0','0'),
	('생야채','양파','50','50','0','0'),
	('생야채','오이','25','25','0','0'),
	('생야채','풋고추','25','0','0','0');
    
INSERT INTO material(category, mname, kcal, chydrate, protein, fat)
	VALUES
    ('유제품','쉐이크(딸기)','325','225','50','75'),
    ('유제품','쉐이크(밀크)','325','200','50','75'),
    ('유제품','쉐이크(초코)','375','250','50','100'),
	('유제품','아이스크림(딸기)','200','100','25','75'),
	('유제품','아이스크림(바닐라)','225','75','25','125'),
	('유제품','아이스크림(소프트)','200','125','25','50'),
	('유제품','아이스크림(초코)','225','125','25','100'),
    ('유제품','요구르트(바이오거트)','125','75','25','25'),
    ('유제품','요구르트(불가리스)','150','100','25','50'),
    ('유제품','요구르트(비피더스)','75','50','25','0'),
    ('유제품','요구르트(액상)','50','50','0','0'),
    ('유제품','요구르트(호상)','100','75','25','25'),
    ('유제품','요구르트(이오)','75','75','0','0'),
    ('유제품','요구르트(파스퇴르)','75','50','25','0'),
    ('유제품','우유','125','50','25','50'),
    ('유제품','우유(딸기)','175','125','25','25'),
    ('유제품','우유(저지방)','100','50','25','25'),
    ('유제품','우유(초코)','125','75','25','25'),
    ('유제품','치즈','62.5','0','12.5','50');
    
INSERT INTO material(category, mname, kcal, chydrate, protein, fat)
	VALUES('음료','','','','','');
    
INSERT INTO material(category, mname, kcal, chydrate, protein, fat)
	VALUES('차','','','','','');
    
INSERT INTO material(category, mname, kcal, chydrate, protein, fat)
	VALUES('주류','','','','','');
    
INSERT INTO material(category, mname, kcal, chydrate, protein, fat)
	VALUES
    ('시리얼','아몬드후레이크','375','275','25','50'),
	('시리얼','콘푸로스트','350','325','25','0');
    
INSERT INTO material(category, mname, kcal, chydrate, protein, fat)
	VALUES('조미료','','','','','');
    
INSERT INTO material(category, mname, kcal, chydrate, protein, fat)
	VALUES('떡','','','','','');
    
INSERT INTO material(category, mname, kcal, chydrate, protein, fat)
	VALUES('어육가공품','','','','','');

SELECT * from material
