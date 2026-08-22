% Exericse 5: Write a program which helps you to make yourself familiar
% with the concept of aliasing, zero-padding and windowing.

%Solution
clc;
clf;

%% Parameterauswahl
% Signal 1 - Parameter
f1 = 1;         % Frequency in Hz
T1 = 200;         % Duration
fA1 = 10;       % Sampling frequency
T1_ZeroPadding = 0;  %  ZeroPadding

% Signal 2 - Parameter
f2 = 1;         % Frequency
T2 = 10;         % Duration
fA2 = 10;       % Sampling frequency
T2_ZeroPadding = 200;  % ZZeroPadding

% Parameter DFT
df1 = 1/(T1+T1_ZeroPadding);    
df2 = 1/(T2+T2_ZeroPadding);     

dT1 = 1/fA1;    
dT2 = 1/fA2;    

N1 = round(T1/dT1);   
N2 = round(T2/dT2);   

N1_ZeroPadding = round(T1_ZeroPadding/dT1);   
N2_ZeroPadding = round(T2_ZeroPadding/dT2);    


%% Signals
% Signal 1 
t1 = 0:dT1:(N1-1)*dT1;
win1 = transpose(rectwin(N1));
corFac1 = N1/sum(win1);
x1 = [win1 .* sin(2*pi*f1*t1), zeros(1,N1_ZeroPadding)];
x1 = [win1 .* (sin(2*pi*f1*t1)+ cos(2*pi*f1*0.98*t1)),zeros(1,N1_ZeroPadding)]; %A4

% Signal 2 
t2 = 0:dT2:(N2-1)*dT2;
win2 = transpose(rectwin(N2));
%win2 = transpose(hann(N2)); %A5
corFac2 = N2/sum(win2);
%x2 = [win2 .* sin(2*pi*f2*t2), zeros(1,N2_ZeroPadding)];
x2 = [win2 .* (sin(2*pi*f2*t2)+cos(2*pi*f2*0.98*t2)),zeros(1,N2_ZeroPadding)]; %A4

%% Spectrum
% Signal 1
X1 = fft(x1/length(x1))*corFac1;
X1 = fftshift(X1);
F1 = (-(N1+N1_ZeroPadding)/2*df1:df1:((N1+N1_ZeroPadding)/2-1)*df1);

% Signal 2
X2 = fft(x2/length(x2))*corFac2;
X2 = fftshift(X2);
F2 = (-(N2+N2_ZeroPadding)/2*df2:df2:((N2+N2_ZeroPadding)/2-1)*df2);

%% Figure
%Plot 1
subplot(311)
plot(t1,x1(1:N1));
hold on;
plot(t2,x2(1:N2));
grid on;
xlabel('t in s');
ylabel('x[t]');
legend('x1','x2');

%Plot 2
subplot(312)
n1=0:length(x1)-1;
n2=0:length(x2)-1;
stem(n1,x1)
hold on;
stem(n2,x2)
grid on;
xlabel('n')
ylabel('x[n]')
legend('x1','x2');

%Plot 3
subplot(313)
plot(F1,abs(X1));
hold on;
plot(F2,abs(X2));
grid on;
ylabel('Betragsgang');
xlabel('Frequenz f in Hz');
legend('X1','X2');