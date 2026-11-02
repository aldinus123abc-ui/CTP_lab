f = 1000;      

f = 1000;      
fs = 50000;     


dt = 1 / fs;


num_samples = 128;
n = 0 : (num_samples - 1);
t = n * dt;              


amplitude = 1;
signal = amplitude * sin(2 * pi * f * t);


figure;
stem(t, signal, 'filled', 'LineWidth', 1.2, 'MarkerSize', 4);


title('Discrete Sinusoidal Signal (128 samples)');
xlabel('Time (seconds)');
ylabel('Amplitude');
grid on;
dt = 1 / fs;

num_samples = 128;
n = 0 : (num_samples - 1); 
t = n * dt;                

amplitude = 1;
signal = amplitude * sin(2 * pi * f * t);


figure;
stem(t, signal, 'filled', 'LineWidth', 1.2, 'MarkerSize', 4);


title('Discrete Sinusoidal Signal (128 samples)');
xlabel('Time (seconds)');
ylabel('Amplitude');
grid on;