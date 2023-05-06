DROP VIEW IF EXISTS `v_studentinfo`;
CREATE VIEW `v_studentinfo` AS
select `tb_student`.`stuID` AS `stuID`, 
`tb_student`.`stuName` AS `stuName`, 
`tb_student`.`age` AS `age`, 
`tb_student`.`sex` AS `sex`, 
`tb_student`.`phone` AS `phone`, 
`tb_student`.`address` AS `address`,
`tb_class`.`className` AS `className`,
`tb_grade`.`gradeName` AS `gradeName`
from ((`tb_student` join `tb_class`) join `tb_grade`)
where ((`tb_student`.`classID` = `tb_class`.`classID`) and 
(`tb_student`.`gradeID` = `tb_grade`.`gradeID`));


DROP VIEW IF EXISTS `v_resultinfo`;
CREATE VIEW `v_resultinfo` AS
select `tb_result`.`ID` AS `ID`,
`tb_result`.`stuID` AS `stuID`,
`v_studentinfo`.`stuName` AS `stuName`,
`tb_examkinds`.`kindName` AS `kindName`,
`tb_subject`.`subName` AS `subName`,
`v_studentinfo`.`className` AS `className`,
`v_studentinfo`.`gradeName` AS `gradeName`,
`tb_result`.`result` AS `result`
from (((`tb_subject` join `tb_result`) join `tb_examkinds`) join `v_studentinfo`)
where ((`tb_result`.`stuID` = `v_studentinfo`.`stuID`) and 
(`tb_result`.`kindID` = `tb_examkinds`.`kindID`) and
(`tb_result`.`subID` = `tb_subject`.`subID`)
);

insert into tb_user values("千月木", "2P02Y3Q502T");