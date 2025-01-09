'use client';

import "./globals.css";
import "../styles/styles.scss";
import "../i18n.client"; // Asegúrate de importar i18n aquí

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="es">
      <head>
        <link
          href="https://fonts.cdnfonts.com/css/modern-typewriter"
          rel="stylesheet"
        />
      </head>
      <body>{children}</body>
    </html>
  );
}
