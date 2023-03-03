clc

function B = iterate_fixed_point(C, rho)
  C_factorial = arrayfun(@factorial, C);

  b = [1 0 0 0;
       1 1 0 0;
       1 1 1 0;
       1 0 1 1];
  
  B_prime = [0; 0; 0; 0];
  B =  [0; 0; 0; 0];
  
  epsilon = 0.001; # for convergence
  difference = epsilon + 1;
  while difference > epsilon
    sigma = b.' * (rho .* (1 - B)) ./ (1 - B_prime);

    sigma_sum = [1; 1; 1; 1]; # first term is always 1
    for l = 1:4
      denom = 1;
      for i = 1:C(l)
        denom = denom * i;
        sigma_sum(l) = sigma_sum(l) + (sigma(l)^i / denom);
      end
    end

    B_prime = sigma .^ C ./ C_factorial ./ sigma_sum;

    B_old = B;

    B(1) = B_prime(1);
    B(2) = 1 - (1 - B_prime(1)) * (1 - B_prime(2));
    B(3) = 1 - (1 - B_prime(1)) * (1 - B_prime(2)) * (1 - B_prime(3));
    B(4) = 1 - (1 - B_prime(1)) * (1 - B_prime(3)) * (1 - B_prime(4));

    difference = max(abs(B - B_old));
  end
end

rho = [2.0; 0.8; 0.8; 0.8];
C = [3; 1; 1; 1];

iterate_fixed_point(C, rho)

N = 50;
B = zeros(N, 4);
for n = 1:N
  rho1 = n .* rho;
  C1 = n .* C;

  B(n, :) = iterate_fixed_point(C1, rho1);
end

hold all
plot(1:N, B)
legend('B_1', 'B_2', 'B_3', 'B_4')
xlabel('iteration')
ylabel('B_k')