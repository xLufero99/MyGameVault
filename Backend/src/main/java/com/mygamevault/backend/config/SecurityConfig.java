package com.mygamevault.backend.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.web.SecurityFilterChain;

// TEMPORAL (solo desarrollo/prueba): permite todo sin autenticacion
// para probar la conexion con Supabase. Quitar cuando se implemente auth real.
@Configuration
public class SecurityConfig {

	@Bean
	SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
		http
				.csrf(csrf -> csrf.disable())
				.authorizeHttpRequests(auth -> auth.anyRequest().permitAll());
		return http.build();
	}
}