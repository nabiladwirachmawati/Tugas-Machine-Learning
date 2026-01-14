@echo off
REM Batch file untuk menjalankan Prediksi Risiko Penyakit Jantung
REM Dibuat untuk memudahkan menjalankan server tanpa perlu mengetik command di terminal

echo ========================================
echo   Prediksi Risiko Penyakit Jantung
echo ========================================
echo.
echo Starting server...
echo Server akan berjalan di: http://localhost:8000
echo.
echo Tekan CTRL+C untuk menghentikan server
echo.

python -m uvicorn main:app --host 127.0.0.1 --port 8000 --reload

pause
