CREATE DATABASE IF NOT EXISTS top_conference;
USE top_conference;
DROP TABLE IF EXISTS CONFERENCE;
CREATE TABLE CONFERENCE (
  topic VARCHAR(190) NOT NULL,
  deadline VARCHAR(8) NOT NULL,
  url VARCHAR(190) NOT NULL,
  start_date VARCHAR(8) NOT NULL,
  end_date VARCHAR(8) NOT NULL,
  address VARCHAR(190) NOT NULL,
  img VARCHAR(190) NOT NULL,
  h5index VARCHAR(5) NOT NULL,
  info TEXT NOT NULL,
  PRIMARY KEY(topic)
);

--example data
insert into CONFERENCE (topic, deadline, url, start_date,end_date, address, img, h5index, info)
values ('cs2017: the best', '20171010','http://latin2018.dc.uba.ar'
,'20171001','20171210','Buenos Aires, Argentina','http://guide2research.com//img/Springer_s.png','100',
'Call for Papers</br>LATIN 2018</br>The 13th Latin American Theoretical Informatics Symposium');