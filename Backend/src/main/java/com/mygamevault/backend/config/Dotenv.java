package com.mygamevault.backend.config;

import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

public final class Dotenv {

	private Dotenv() {
	}

	public static void load(String filename) {
		Path path = Paths.get(filename);
		if (!Files.exists(path)) {
			throw new IllegalStateException(
					"Archivo " + filename + " no encontrado en " + Paths.get("").toAbsolutePath());
		}
		try {
			for (String rawLine : Files.readAllLines(path, StandardCharsets.UTF_8)) {
				String line = rawLine.trim();
				if (line.isEmpty() || line.startsWith("#")) {
					continue;
				}
				int idx = line.indexOf('=');
				if (idx <= 0) {
					continue;
				}
				String key = line.substring(0, idx).trim();
				String value = line.substring(idx + 1).trim();
				if (value.length() >= 2 && (value.charAt(0) == '"' || value.charAt(0) == '\'')
						&& value.charAt(value.length() - 1) == value.charAt(0)) {
					value = value.substring(1, value.length() - 1);
				}
				if (System.getenv(key) == null && System.getProperty(key) == null) {
					System.setProperty(key, value);
				}
			}
		} catch (IOException e) {
			throw new IllegalStateException("No se pudo leer " + filename, e);
		}
	}
}