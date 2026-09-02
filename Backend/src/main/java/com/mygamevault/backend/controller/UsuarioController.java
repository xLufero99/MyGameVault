package com.mygamevault.backend.controller;

import java.util.List;
import java.util.Map;

import org.springframework.dao.DataIntegrityViolationException;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.mygamevault.backend.dto.UsuarioRequest;
import com.mygamevault.backend.model.Usuario;
import com.mygamevault.backend.repository.UsuarioRepository;

@RestController
@RequestMapping("/api/usuarios")
public class UsuarioController {

	private final UsuarioRepository usuarioRepository;

	public UsuarioController(UsuarioRepository usuarioRepository) {
		this.usuarioRepository = usuarioRepository;
	}

	@PostMapping
	public ResponseEntity<?> crear(@RequestBody UsuarioRequest request) {
		if (request.nombre() == null || request.nombre().isBlank()
				|| request.email() == null || request.email().isBlank()) {
			return ResponseEntity.badRequest().body(Map.of("error", "Los campos 'nombre' y 'email' son obligatorios."));
		}
		Usuario usuario = new Usuario();
		usuario.setNombre(request.nombre());
		usuario.setEmail(request.email());
		try {
			Usuario creado = usuarioRepository.save(usuario);
			return ResponseEntity.status(HttpStatus.CREATED).body(creado);
		} catch (DataIntegrityViolationException e) {
			return ResponseEntity.badRequest().body(Map.of("error", "Ya existe un usuario con ese email."));
		}
	}

	@GetMapping
	public ResponseEntity<List<Usuario>> listar() {
		return ResponseEntity.ok(usuarioRepository.findAll());
	}
}