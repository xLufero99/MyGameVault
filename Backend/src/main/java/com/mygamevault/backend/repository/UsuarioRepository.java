package com.mygamevault.backend.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import com.mygamevault.backend.model.Usuario;

public interface UsuarioRepository extends JpaRepository<Usuario, Long> {
}