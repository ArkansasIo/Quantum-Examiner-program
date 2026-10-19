CREATE DATABASE IF NOT EXISTS quantum_examiner CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE quantum_examiner;

CREATE TABLE IF NOT EXISTS devices (
 id BIGINT PRIMARY KEY AUTO_INCREMENT,
 name VARCHAR(128) NOT NULL,
 adapter_type VARCHAR(64) NOT NULL,
 serial_number VARCHAR(128),
 calibration_version VARCHAR(64),
 created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS electrical_samples (
 id BIGINT PRIMARY KEY AUTO_INCREMENT,
 device_id BIGINT,
 sample_time TIMESTAMP(6) NOT NULL,
 channel_name VARCHAR(128) NOT NULL,
 voltage DOUBLE,
 current DOUBLE,
 frequency_hz DOUBLE,
 raw_json JSON,
 FOREIGN KEY(device_id) REFERENCES devices(id)
);

CREATE TABLE IF NOT EXISTS experiments (
 id BIGINT PRIMARY KEY AUTO_INCREMENT,
 name VARCHAR(255) NOT NULL,
 qubit_count INT NOT NULL,
 configuration_json JSON NOT NULL,
 created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS examinations (
 id BIGINT PRIMARY KEY AUTO_INCREMENT,
 experiment_id BIGINT,
 bloch_x DOUBLE,
 bloch_y DOUBLE,
 bloch_z DOUBLE,
 purity DOUBLE,
 physical BOOLEAN NOT NULL,
 warnings_json JSON,
 provenance_json JSON,
 created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
 FOREIGN KEY(experiment_id) REFERENCES experiments(id)
);
