function [output_vector] = FiniteDiff(input_vector,dt,varargin)
% This function approximates the derivative of input_vector using a centered finite
% difference scheme of order norder.
%
% This function uses centerd finite difference scheme to compute a vector's
% derivative. The output vector will have the same size as the input_vector
% with some zero-padding at the beginning and end. 
%
% The order input is optionnal, by default it will be set to 4
% 
% Inputs : -input_vector is vector whose derivative have to be computed
%          -dt is the time step of the input vector (!!! needs to be
%          constant time step)
%          -(norder) is the order of the finite difference scheme to be
%          applied
% Outputs : -output_vector is the obtained differentiated vector
% 
% @Antoine de Comite - May 2021
% antoinedecomite@gmail.com


%% 0. Defensive programming
switch nargin
    case 1
        error('One argument mission, please refer to the signature');
    case 2
        order = 4;
    case 3
        order = varargin{1};
end

if mod(order,2)~=0
    error('The order should be an even number (2 or 4)');
elseif (order<2 || order>4)
    error('The order should be an even number (2 or 4)');
end

%% 1. Function core 

output_vector = zeros(length(input_vector),1);
switch order
    case 2
        output_vector(2:end-1) = (input_vector(3:end)-input_vector(1:end-2))/(2*dt);
    case 4
        output_vector(3:end-2) = (-input_vector(5:end)+8*input_vector(4:end-1)-8*input_vector(2:end-3)+input_vector(1:end-4))/(12*dt);
end


end
