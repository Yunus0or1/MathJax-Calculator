from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json
import math

# Create your views here.


def home(request):
	
	
	return render(request, 'homepage.html', {
		})

def calculator_main_page(request):
	
	return render(request, 'calculator_main_page.html', {
		})

		
def calculator1(request):

	if request.method == 'GET':
	
		result = 0
		return render(request, 'calculator1.html', {'result' : result})
		
		
	if request.method == 'POST':
	
		f = int(request.POST['f'])
		a = int(request.POST['a'])
		l = int(request.POST['l'])
		b = int(request.POST['b'])
		h = int(request.POST['h'])
		e = int(request.POST['e'])
		x = int(request.POST['x'])
		
		
		#Input unit fetching
		unit1_input = request.POST['unit1_input']		
		unit2_input = request.POST['unit2_input']
		unit3_input = request.POST['unit3_input']
		unit4_input = request.POST['unit4_input']
		
			
		unit1_input_numeric = 1
		unit2_input_numeric = 1
		unit3_input_numeric = 1
		unit4_input_numeric = 1
		
		

		
		
		#first converting input unit to base inputs. Newton, Meter and MegaPascal are the base unit
		
		if unit1_input == 'kilonewton':
			unit1_input_numeric = 1000
			
		if unit2_input == 'milimeter':
			unit2_input_numeric = 1/1000
			
		if unit3_input == 'milimeter':
			unit3_input_numeric = 1/1000			
		
		if unit4_input == 'gpa':
			unit4_input_numeric = 1000
			

		
		
		#Calculation result based on base unit	
		
		I = (b*unit2_input_numeric) * (h*unit3_input_numeric)**3 / 12	
		M = -(f*unit1_input_numeric) * (a*unit2_input_numeric)
		
		moment_M_x = 0
		shear_stress_V_x = 0
		
		
		if x>0 and x<=l :
			moment_M_x = -a * x * f / l 
			shear_stress_V_x = (-f * a * l**2)*((x/l) - (x/l)**3)/ (6 * e * I)

			
		# Desired Output unit fetching
		unit1_output = request.POST['unit1_output']
						
		unit1_output_numeric = 1
		
		
		#Now converting the input to the specified desired unit.
		
		if unit1_output == 'newton/meter':
			I = I
		if unit1_output == 'newton/milimeter':
			I = I * (1000*1000)				
			
		
		
		result = 1
		
		#Formatting result
		I = '{:.2e}'.format(I)	
		M = '{:.2e}'.format(M)
		if x>0 and x<=l :
			moment_M_x = '{:.2e}'.format(moment_M_x)
			shear_stress_V_x = '{:.2e}'.format(shear_stress_V_x)
		
		
		return render(request, 'calculator1.html',
		{
		'result' : result,
		'I' : I,
		'M' : M,
		'moment_M_x' : moment_M_x,
		'shear_stress_V_x' : shear_stress_V_x,	
		'unit1' : unit1_input,
		'unit2' : unit2_input,
		'unit3' : unit3_input,
		'unit1_output' : unit1_output,
		
		
		'f':f,
		'a':a,
		'l':l,
		'b':b,
		'h':h,
		'e':e,
		'x':x,	
		})
		
		




def calculator2(request):

	if request.method == 'GET':
	
		result = 0
		return render(request, 'calculator2.html', {'result' : result})

	if request.method == 'POST':
	
		f = float(request.POST['f_input'])
		x = float(request.POST['x_input'])
		a = float(request.POST['a_input'])
		i = float(request.POST['i_input'])
		e = float(request.POST['e_input'])
		l = float(request.POST['l_input'])
		b = float(request.POST['b_input'])
		
		
		# Defining The base units.
		# A = N
		# B = N 
		# M(x) = N.m
		# M_max = N.m
		# f = m
		# v(x) = m
		# x_m = m
		# f_m = m
		# angle_a = rad
		# angle_b = rad
		
		
		
		#Taking input units
		
		unit_f_input = request.POST['unit_f_input']
		unit_x_input = request.POST['unit_x_input']	
		unit_a_input = request.POST['unit_a_input']	
		unit_i_input = request.POST['unit_i_input']	
		unit_e_input = request.POST['unit_e_input']	
		unit_l_input = request.POST['unit_l_input']
		unit_b_input = request.POST['unit_b_input']
		
	

		
	
		
		
		unit_f_numeric = 1
		unit_x_numeric = 1
		unit_a_numeric = 1
		unit_i_numeric = 1		
		unit_e_numeric = 1	
		unit_l_numeric = 1	
		unit_b_numeric = 1	
		
		#Converting f base unit is N
		
		if unit_f_input == 'N':
			unit_f_numeric = 1
		
		if unit_f_input == 'kN':
			unit_f_numeric = 1000
		
		if unit_f_input == 'MN':
			unit_f_numeric = 1000*1000		
		
		if unit_f_input == 'lbf':
			unit_f_numeric = 0.224809
			
		
		#Converting x base unit is m
		
		if unit_x_input == 'm':
			unit_x_numeric = 1
		
		if unit_x_input == 'mm':
			unit_x_numeric = 1/1000
		
		if unit_x_input == 'cm':
			unit_x_numeric = 1/100		
		
		if unit_x_input == 'in':
			unit_x_numeric = 1/39.37	
			
		if unit_x_input == 'ft':
			unit_x_numeric = 1/3.28	

		#Converting a base unit is m
		
		if unit_a_input == 'm':
			unit_a_numeric = 1
		
		if unit_a_input == 'mm':
			unit_a_numeric = 1/1000
		
		if unit_a_input == 'cm':
			unit_a_numeric = 1/100		
		
		if unit_a_input == 'in':
			unit_a_numeric = 1/39.37	
			
		if unit_a_input == 'ft':
			unit_a_numeric = 1/3.28	
			
		#Converting I base unit is m^4
		
		if unit_i_input == 'm':
			unit_i_numeric = 1
		
		if unit_i_input == 'mm':
			unit_i_numeric = 1/(1000*1000*1000*1000)
		
		if unit_i_input == 'cm':
			unit_i_numeric = 1/(10*10*10*10)		
		
		if unit_i_input == 'in':
			unit_i_numeric = 1/(39.37*39.37*39.37*39.37)	
			
		if unit_i_input == 'ft':
			unit_i_numeric = 1/(3.28*3.28*3.28*3.28)

		#Converting E base unit is Pa
		
		if unit_e_input == 'Pa':
			unit_e_numeric = 1
		
		if unit_e_input == 'GPa':
			unit_e_numeric = 1000000000
			
		if unit_e_input == 'MPa':
			unit_e_numeric = 1000000	
			
		if unit_e_input == 'N/mm_2':
			unit_e_numeric = 1000*1000	
		
			
		#Converting l base unit is m
		
		if unit_l_input == 'm':
			unit_l_numeric = 1
		
		if unit_l_input == 'mm':
			unit_l_numeric = 1/1000
		
		if unit_l_input == 'cm':
			unit_l_numeric = 1/100		
		
		if unit_l_input == 'in':
			unit_l_numeric = 1/39.37		
		
		if unit_l_input == 'ft':
			unit_l_numeric = 1/3.28	
			
		
		#Converting b base unit is m
		if unit_b_input == 'm':
			unit_b_numeric = 1
		
		
		# Now converting input variable with their units
		
		f = f * unit_f_numeric
		x = x * unit_x_numeric
		a = a * unit_a_numeric
		i = i * unit_i_numeric
		e = e * unit_e_numeric
		l = l * unit_l_numeric
		b = b * unit_b_numeric
		




		#Calculating A  base unit is kN
		A = (f ) * ( b ) / ( l )
		
		unit_a_output = request.POST['unit_a_output']

		
		#Converting A to desired unit.
		if unit_a_output == 'N':
			A = A 			
		if unit_a_output == 'kN':
			A = A / 1000
		if unit_a_output == 'MN':
			A = A / 1000000	
		if unit_a_output == 'lbf':
			A = A / 4.44

		
		
		
		
		#Calculating B  base unit is kN
		B = (f ) * ( a ) / ( l )
		
		unit_b_output = request.POST['unit_b_output']

		
		#Converting B to desired unit.
		if unit_b_output == 'N':
			B = B 			
		if unit_b_output == 'kN':
			B = B / 1000
		if unit_b_output == 'MN':
			B = B / (1000*1000)	
		if unit_b_output == 'lbf':
			B = B / 4.44	

		
		#Calculating M(x)  base unit is kN
		if x<=a :
			M_x = (f ) * ( b )* ( x ) / ( l )
		if x>a :
			M_x = (f ) * ( a )*(1-(( x ) / ( l )))
		
		unit_m_x_output = request.POST['unit_m_x_output']

		
		#Converting M(x) to desired unit .
		if unit_m_x_output == 'N.m':
			M_x = M_x 			
		if unit_m_x_output == 'kN.m':
			M_x = M_x / 1000
		if unit_m_x_output == 'N.mm':
			M_x = M_x * 1000	
		if unit_m_x_output == 'lbf.ft':
			M_x = M_x * 0.224809 * 3.28		
		
		
		#Calculating M_max  base unit is N

		M_max = (f ) *( a ) * ( b ) / ( l )
	
		unit_m_max_output = request.POST['unit_m_max_output']

		
		#Converting M_max to desired unit .
		if unit_m_max_output == 'N.m':
			M_max = M_max 			
		if unit_m_max_output == 'kN.m':
			M_max = M_max / 1000
		if unit_m_max_output == 'N.mm':
			M_max = M_max * 1000
		if unit_m_max_output == 'lbf.ft':
			M_max = M_max * 0.224809 * 3.28	

			
		#Calculating f  base unit is m
		
		f_deflection = ((f ) * ( a )**2 * ( b )**2)  / (3 * ( e ) * (i ) * ( l ) )
		
		unit_f_output = request.POST['unit_f_output']
		


		
		#Converting f to desired unit.
		if unit_f_output == 'm':
			f_deflection = f_deflection 			
		if unit_f_output == 'mm':
			f_deflection = f_deflection * 1000
		if unit_f_output == 'cm':
			f_deflection = f_deflection * 100
		if unit_f_output == 'in':
			f_deflection = f_deflection * 39.37				
		if unit_f_output == 'ft':	
			f_deflection = f_deflection * 3.28084
			
			
			
		#Calculating V(x)  base unit is m	
		if x<=a :
			V_x = (f*a*b**2)*(((1+(l/b))*(x/l)) - (x**3/(a*b*l)))/(6*e*i)
		if x>a :
			V_x = (f*a**2*b)*(((1+(l/a))*((l-x)/l)) - ((l-x)**3/(a*b*l)))/(6*e*i)
		
		unit_v_x_output = request.POST['unit_v_x_output']
		


		
		#Converting V(x) to desired unit.
		if unit_v_x_output == 'm':
			V_x = V_x 			
		if unit_v_x_output == 'mm':
			V_x = V_x * 1000
		if unit_v_x_output == 'cm':
			V_x = V_x * 100
		if unit_v_x_output == 'in':
			V_x = V_x * 39.37				
		if unit_v_x_output == 'ft':	
			V_x = V_x * 3.28084			
			


		#Calculating x_m base unit is m	
		if a>=b :
			x_m = ((l**2 - b**2)/3)**(.5)
		if a<b :
			x_m = l-((l**2 - b**2)/3)**(.5)
		
		unit_x_m_output = request.POST['unit_x_m_output']
		


		
		#Converting x_m to desired unit.
		if unit_x_m_output == 'm':
			x_m = x_m 			
		if unit_x_m_output == 'mm':
			x_m = x_m * 1000
		if unit_x_m_output == 'cm':
			x_m = x_m * 100
		if unit_x_m_output == 'in':
			x_m = x_m * 39.37				
		if unit_x_m_output == 'ft':	
			x_m = x_m * 3.28084		


			
			
		#Calculating f_m base unit is m	
		if a>=b :
			f_m = (f*b)*((l**2 - b**2)**3)**(.5)/(9*3**(0.5)*e*i*l)
		if a<b :
			f_m = (f*a)*((l**2 - a**2)**3)**(.5)/(9*3**(0.5)*e*i*l)
		
		unit_f_m_output = request.POST['unit_f_m_output']
		


		
		#Converting f_m to desired unit.
		if unit_f_m_output == 'm':
			f_m = f_m 			
		if unit_f_m_output == 'mm':
			f_m = f_m * 1000
		if unit_f_m_output == 'cm':
			f_m = f_m * 100
		if unit_f_m_output == 'in':
			f_m = f_m * 39.37				
		if unit_f_m_output == 'ft':	
			f_m = f_m * 3.28084				
			
			
		#Calculating alpha_a base unit is radian	
		
		alpha_a = (f*a*b*(l+b))/(6*e*i*l)
		
		unit_alpha_a_output = request.POST['unit_alpha_a_output']
		
		if unit_alpha_a_output == 'rad' : 
			alpha_a = alpha_a

		if unit_alpha_a_output == 'deg' : 
			alpha_a = alpha_a * 57.2958
			
			
		#Calculating alpha_b base unit is radian
		
		alpha_b = (f*a*b*(l+a))/(6*e*i*l)
		
		unit_alpha_b_output = request.POST['unit_alpha_b_output']
		
		if unit_alpha_b_output == 'rad' : 
			alpha_b = alpha_b

		if unit_alpha_b_output == 'deg' : 
			alpha_b = alpha_b * 57.2958			
			
			

		#Formatting result
		A = '{:.5e}'.format(A)
		B = '{:.5e}'.format(B)
		M_x = '{:.5e}'.format(M_x)
		M_max = '{:.5e}'.format(M_max)
		f_deflection = '{:.5e}'.format(f_deflection)
		V_x = '{:.5e}'.format(V_x)
		x_m = '{:.5e}'.format(x_m)
		f_m = '{:.5e}'.format(f_m)
		alpha_a = '{:.3e}'.format(alpha_a)
		alpha_b = '{:.3e}'.format(alpha_b)
		
		result = 1
		return render(request, 'calculator2.html',
		{
		'result' : result,
				
		'A':A,
		'unit_a_output':unit_a_output,
		
		'B':B,
		'unit_b_output':unit_b_output,
		
		'M_x':M_x,
		'unit_m_x_output':unit_m_x_output,	

		'M_max':M_max,
		'unit_m_max_output':unit_m_max_output,	

		'f_deflection':f_deflection,
		'unit_f_output':unit_f_output,	

		'V_x':V_x,
		'unit_v_x_output':unit_v_x_output,		

		'x_m':x_m,
		'unit_x_m_output':unit_x_m_output,	
		
		'f_m':f_m,
		'unit_f_m_output':unit_f_m_output,	
		
		'alpha_a':alpha_a,
		'unit_alpha_a_output':unit_alpha_a_output,	
		
		'alpha_b':alpha_b,
		'unit_alpha_b_output':unit_alpha_b_output,	
		
		#Input data sending
		'f' : request.POST['f_input'],
		'x' : request.POST['x_input'],
		'a' : request.POST['a_input'],
		'i' : request.POST['i_input'],
		'e' : request.POST['e_input'],
		'l' : request.POST['l_input'],
		'b' : request.POST['b_input'],			
		
		'unit_f_input' : request.POST['unit_f_input'],
		'unit_x_input' : request.POST['unit_x_input'],	
		'unit_a_input' : request.POST['unit_a_input'],	
		'unit_i_input' : request.POST['unit_i_input'],	
		'unit_e_input' : request.POST['unit_e_input'],	
		'unit_l_input' : request.POST['unit_l_input'],
		'unit_b_input' : request.POST['unit_b_input'],
		
		

		})








		
		