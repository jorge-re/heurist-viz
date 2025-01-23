import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

// https://vitejs.dev/config/
export default defineConfig({
  build: {
    chunkSizeWarningLimit: 4000,
    emptyOutDir: true,
    outDir: "../routes/ui/",
  },
  plugins: [react()],
  server: {
    proxy: {
      "/api": "http://0.0.0.0:8935",
    },
  },
});
