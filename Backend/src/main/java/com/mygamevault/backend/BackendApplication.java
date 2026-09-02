package com.mygamevault.backend;

import com.mygamevault.backend.config.Dotenv;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class BackendApplication {

	public static void main(String[] args) {
		Dotenv.load(".env");
		SpringApplication.run(BackendApplication.class, args);
	}

}
