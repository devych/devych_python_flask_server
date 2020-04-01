-- users Table Create SQL
CREATE TABLE users
(
    `id`        INT             NOT NULL    AUTO_INCREMENT COMMENT '아이디',
    `userid`    VARCHAR(45)     NOT NULL    COMMENT '유저아이디',
    `password`  VARCHAR(45)     NOT NULL    COMMENT '패스워드',
    `email`     VARCHAR(100)    NOT NULL    COMMENT '이메일',
    PRIMARY KEY (id)
);


-- users Table Create SQL
CREATE TABLE lotto_draw_info
(
    `id`              INT            NOT NULL    AUTO_INCREMENT COMMENT '아이디',
    `drwNo`           INT            NULL        COMMENT '회차',
    `drwNoDate`       DATE           NULL        COMMENT '추첨일',
    `firstAccumamnt`  VARCHAR(45)    NULL        COMMENT '총1등당첨금',
    `firstPrzwnerCo`  BIGINT         NULL        COMMENT '1등당첨인원',
    `firstWinamnt`    BIGINT         NULL        COMMENT '1등수령액',
    `totSellamnt`     BIGINT         NULL        COMMENT '총판매금액',
    `drwtNo1`         INT            NULL        COMMENT '1번번호',
    `drwtNo2`         INT            NULL        COMMENT '2번번호',
    `drwtNo3`         INT            NULL        COMMENT '3번번호',
    `drwtNo4`         INT            NULL        COMMENT '4번번호',
    `drwtNo5`         INT            NULL        COMMENT '5번번호',
    `drwtNo6`         INT            NULL        COMMENT '6번번호',
    `bnusNo`          INT            NULL        COMMENT '보너스번호',
    PRIMARY KEY (id)
);

ALTER TABLE lotto_draw_info COMMENT '로또당첨히스토리';


-- users Table Create SQL
CREATE TABLE user_created_lotto
(
    `id`            INT            NOT NULL    AUTO_INCREMENT COMMENT '아이디',
    `user`          VARCHAR(45)    NULL        COMMENT '생성자정보',
    `drwtNo1`       INT            NOT NULL    COMMENT '1번번호',
    `drwtNo2`       INT            NOT NULL    COMMENT '2번번호',
    `drwtNo3`       INT            NOT NULL    COMMENT '3번번호',
    `drwtNo4`       INT            NOT NULL    COMMENT '4번번호',
    `drwtNo5`       INT            NOT NULL    COMMENT '5번번호',
    `drwtNo6`       INT            NOT NULL    COMMENT '6번번호',
    `bnusNo`        INT            NOT NULL    COMMENT '보너스번호',
    `created_date`  TIMESTAMP      NOT NULL    COMMENT '생성일',
    PRIMARY KEY (id)
);

ALTER TABLE user_created_lotto COMMENT '로또생성번호';


