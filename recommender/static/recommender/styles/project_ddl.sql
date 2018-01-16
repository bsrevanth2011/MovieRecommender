CREATE TABLE Event_Head
(
  E_H_id VARCHAR(20) NOT NULL,
  E_H_name VARCHAR(20) NOT NULL,
  PRIMARY KEY (E_H_id)
);

CREATE TABLE Events
(
  E_id VARCHAR(20) NOT NULL,
  E_name VARCHAR(20) NOT NULL,
  E_H_id VARCHAR(20) NOT NULL,
  PRIMARY KEY (E_id),
  FOREIGN KEY (E_H_id) REFERENCES Event_Head(E_H_id)
);

CREATE TABLE Winner_2
(
  W_position INT NOT NULL,
  W_prize INT NOT NULL,
  W_score INT NOT NULL,
  PRIMARY KEY (W_score)
);

CREATE TABLE Department_Head
(
  D_h_id VARCHAR(20) NOT NULL,
  D_h_f_name VARCHAR(20) NOT NULL,
  D_h_l_name VARCHAR(20) NOT NULL,
  PRIMARY KEY (D_h_id)
);

CREATE TABLE Department
(
  D_id VARCHAR(20) NOT NULL,
  D_name VARCHAR(20) NOT NULL,
  D_h_id VARCHAR(20) NOT NULL,
  PRIMARY KEY (D_id),
  FOREIGN KEY (D_h_id) REFERENCES Department_Head(D_h_id)
);

CREATE TABLE Teams
(
  T_id VARCHAR(20) NOT NULL,
  T_inst_name VARCHAR(20) NOT NULL,
  T_name VARCHAR(20) NOT NULL,
  T_city VARCHAR(20) NOT NULL,
  PRIMARY KEY (T_id)
);

CREATE TABLE Team_member
(
  T_member_id VARCHAR(20) NOT NULL,
  T_m_name VARCHAR(20) NOT NULL,
  T_dob DATE NOT NULL,
  PRIMARY KEY (T_member_id)
);

CREATE TABLE Team_members_2
(
  T_m_ph_no VARCHAR(10) NOT NULL,
  T_member_id VARCHAR(20) NOT NULL,
  PRIMARY KEY (T_m_ph_no, T_member_id),
  FOREIGN KEY (T_member_id) REFERENCES Team_member(T_member_id)
);

CREATE TABLE Faculty_member
(
  F_id VARCHAR(20) NOT NULL,
  F_name VARCHAR(20) NOT NULL,
  PRIMARY KEY (F_id)
);

CREATE TABLE Judge
(
  J_name VARCHAR(20) NOT NULL,
  J_id VARCHAR(20) NOT NULL,
  J_level INT NOT NULL,
  PRIMARY KEY (J_id)
);

CREATE TABLE Competition
(
  Co_id VARCHAR(20) NOT NULL,
  Co_name VARCHAR(20) NOT NULL,
  Co_date DATE NOT NULL,
  PRIMARY KEY (Co_id)
);

CREATE TABLE Competition_2
(
  Co_venue VARCHAR(20) NOT NULL,
  Co_timing VARCHAR(20) NOT NULL,
  Co_date DATE NOT NULL,
  PRIMARY KEY (Co_date)
);

CREATE TABLE Facilitate
(
  D_h_id VARCHAR(20) NOT NULL,
  T_id VARCHAR(20) NOT NULL,
  PRIMARY KEY (D_h_id, T_id),
  FOREIGN KEY (D_h_id) REFERENCES Department_Head(D_h_id),
  FOREIGN KEY (T_id) REFERENCES Teams(T_id)
);

CREATE TABLE contain
(
  T_member_id VARCHAR(20) NOT NULL,
  F_id VARCHAR(20) NOT NULL,
  T_id VARCHAR(20) NOT NULL,
  PRIMARY KEY (T_member_id, F_id, T_id),
  FOREIGN KEY (T_member_id) REFERENCES Team_member(T_member_id),
  FOREIGN KEY (F_id) REFERENCES Faculty_member(F_id),
  FOREIGN KEY (T_id) REFERENCES Teams(T_id)
);

CREATE TABLE Food_and_lodging
(
  F_type INT NOT NULL,
  D_id VARCHAR(20) NOT NULL,
  FOREIGN KEY (D_id) REFERENCES Department(D_id)
);

CREATE TABLE Security
(
  D_id VARCHAR(20) NOT NULL,
  FOREIGN KEY (D_id) REFERENCES Department(D_id)
);

CREATE TABLE Decor
(
  D_id VARCHAR(20) NOT NULL,
  FOREIGN KEY (D_id) REFERENCES Department(D_id)
);

CREATE TABLE Finance_Committee
(
  Fc_count INT NOT NULL,
  Fc_m_name VARCHAR(20) NOT NULL,
  Fc_m_id VARCHAR(20) NOT NULL,
  F_date DATE NOT NULL,
  E_id VARCHAR(20) NOT NULL,
  PRIMARY KEY (Fc_m_id),
  FOREIGN KEY (E_id) REFERENCES Events(E_id)
);
CREATE TABLE Winner
(
  W_id VARCHAR(20) NOT NULL,
  W_name VARCHAR(20) NOT NULL,
  W_score INT NOT NULL,
  decided_J_id VARCHAR(20) NOT NULL,
  PRIMARY KEY (W_id,W_score),
  FOREIGN KEY (decided_J_id) REFERENCES Judge(J_id)
);

CREATE TABLE Consists_of
(
  D_id VARCHAR(20) NOT NULL,
  E_id VARCHAR(20) NOT NULL,
  Co_id VARCHAR(20) NOT NULL,
  PRIMARY KEY (D_id, E_id, Co_id),
  FOREIGN KEY (D_id) REFERENCES Department(D_id),
  FOREIGN KEY (E_id) REFERENCES Events(E_id),
  FOREIGN KEY (Co_id) REFERENCES Competition(Co_id)
);

CREATE TABLE Take_part_in
(
  T_id VARCHAR(20) NOT NULL,
  J_id VARCHAR(20) NOT NULL,
  Co_id VARCHAR(20) NOT NULL,
  PRIMARY KEY (T_id, J_id, Co_id),
  FOREIGN KEY (T_id) REFERENCES Teams(T_id),
  FOREIGN KEY (J_id) REFERENCES Judge(J_id),
  FOREIGN KEY (Co_id) REFERENCES Competition(Co_id)
);

CREATE TABLE Give_prizes
(
  Amount INT NOT NULL,
  Shield INT NOT NULL,
  J_id VARCHAR(20) NOT NULL,
  W_id VARCHAR(20) NOT NULL,
  PRIMARY KEY (J_id, W_id),
  FOREIGN KEY (J_id) REFERENCES Judge(J_id),
  FOREIGN KEY (W_id) REFERENCES Winner(W_id)
);
