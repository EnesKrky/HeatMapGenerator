from math import *
import pygame,pygame.gfxdraw,random
pygame.init()

def pixelcolor(pos,pos1,pos2,pos3,col1,col2,col3):
    v1=[pos2[0]-pos1[0],pos2[1]-pos1[1]]
    v2=[pos3[0]-pos1[0],pos3[1]-pos1[1]]
    det=v1[0]*v2[1]-v2[0]*v1[1]
    t=((pos[0]-pos1[0])*v2[1]-(pos[1]-pos1[1])*v2[0])/det
    s=((pos[1]-pos1[1])*v1[0]-(pos[0]-pos1[0])*v1[1])/det
    v1_color=[col2[0]-col1[0],col2[1]-col1[1],col2[2]-col1[2]]
    v2_color=[col3[0]-col1[0],col3[1]-col1[1],col3[2]-col1[2]]
    pixcol=(col1[0]+t*v1_color[0]+s*v2_color[0],col1[1]+t*v1_color[1]+s*v2_color[1],col1[2]+t*v1_color[2]+s*v2_color[2])
    return pixcol

def trianglepainter(X,Y,Z,Hcol,Mcol,Ccol,scr,cntr,z):
    Zmax=max(Z[0])
    Zmin=min(Z[0])
    for i in Z[1:]:
        if max(i)>Zmax:
            Zmax=max(i)
        if min(i)<Zmin:
            Zmin=min(i)
            
    colors=[]
    for i in range(len(X)):
        rowcolors=[]
        for k in range(len(X[0])):
            if Zmax!=Zmin:
                ratio=1-(Z[i][k]-Zmin)/(Zmax-Zmin)
                if ratio<=0.5:
                    dR=Mcol[0]-Hcol[0]
                    dG=Mcol[1]-Hcol[1]
                    dB=Mcol[2]-Hcol[2]
                    if dR!=0:
                        R=Mcol[0]+2*(ratio-0.5)*dR
                    else:
                        R=Mcol[0]
                    if dG!=0:
                        G=Mcol[1]+2*(ratio-0.5)*dG
                    else:
                        G=Mcol[1]
                    if dB!=0:
                        B=Mcol[2]+2*(ratio-0.5)*dB
                    else:
                        B=Mcol[2]
                elif ratio>0.5:
                    dR=Ccol[0]-Mcol[0]
                    dG=Ccol[1]-Mcol[1]
                    dB=Ccol[2]-Mcol[2]
                    if dR!=0:
                        R=Ccol[0]+2*(ratio-1)*dR
                    else:
                        R=Mcol[0]
                    if dG!=0:
                        G=Ccol[1]+2*(ratio-1)*dG
                    else:
                        G=Mcol[1]
                    if dB!=0:
                        B=Ccol[2]+2*(ratio-1)*dB
                    else:
                        B=Mcol[2]
            else:
                R=Ccol[0]
                G=Ccol[1]
                B=Ccol[2]
            rowcolors.append((R,G,B))
        colors.append(rowcolors)
        
    trianglenumber=int(2*(len(X[0])-1)*(len(X)-1))
    contourmatrix=[]
    for i in range(trianglenumber):
        k=i//(2*(len(X[0])-1))
        j=i-k*2*(len(X[0])-1)
        if j%2==0:
            if cntr:
                v1=(X[k][int(j/2)+1]-X[k][int(j/2)],Y[k][int(j/2)+1]-Y[k][int(j/2)],Z[k][int(j/2)+1]-Z[k][int(j/2)])
                v2=(X[k+1][int(j/2)]-X[k][int(j/2)],Y[k+1][int(j/2)]-Y[k][int(j/2)],Z[k+1][int(j/2)]-Z[k][int(j/2)])
                for h in range(11):
                    if v2[2]!=0:
                        t=h/10
                        s=(z-Z[k][int(j/2)]-v1[2]*t)/v2[2]
                        if 0<=s<=1-t and [X[k][int(j/2)]+t*v1[0]+s*v2[0],Y[k][int(j/2)]+t*v1[1]+s*v2[1],Z[k][int(j/2)]+t*v1[2]+s*v2[2]] not in contourmatrix:
                            contourmatrix.append([X[k][int(j/2)]+t*v1[0]+s*v2[0],Y[k][int(j/2)]+t*v1[1]+s*v2[1],Z[k][int(j/2)]+t*v1[2]+s*v2[2]])
            for Ypix in range(round(Y[k][int(j/2)]),round(Y[k+1][int(j/2)])):
                maxXval=(Y[k+1][int(j/2)]-Ypix)*(X[k][int(j/2)+1]-X[k][int(j/2)])/(Y[k+1][int(j/2)]-Y[k][int(j/2)])+X[k][int(j/2)]
                for Xpix in range(round(X[k][int(j/2)]),round(maxXval)):
                    color=pixelcolor((Xpix,Ypix),(round(X[k][int(j/2)]),round(Y[k][int(j/2)])),(round(X[k][int(j/2)+1]),round(Y[k][int(j/2)+1])),(round(X[k+1][int(j/2)]),round(Y[k+1][int(j/2)])),colors[k][int(j/2)],colors[k][int(j/2)+1],colors[k+1][int(j/2)])
                    if 0<=color[0]<=255 and 0<=color[1]<=255 and 0<=color[2]<=255:
                        scr.set_at((Xpix,Ypix),color)
        else:
            if cntr:
                v1=(X[k][int((j+1)/2)]-X[k+1][int((j+1)/2)],Y[k][int((j+1)/2)]-Y[k+1][int((j+1)/2)],Z[k][int((j+1)/2)]-Z[k+1][int((j+1)/2)])
                v2=(X[k+1][int((j-1)/2)]-X[k+1][int((j+1)/2)],Y[k+1][int((j-1)/2)]-Y[k+1][int((j+1)/2)],Z[k+1][int((j-1)/2)]-Z[k+1][int((j+1)/2)])
                for h in range(11):
                    if v2[2]!=0:
                        t=h/10
                        s=(z-Z[k+1][int((j+1)/2)]-v1[2]*t)/v2[2]
                        if 0<=s<=1-t and [X[k+1][int((j+1)/2)]+t*v1[0]+s*v2[0],Y[k+1][int((j+1)/2)]+t*v1[1]+s*v2[1],Z[k+1][int((j+1)/2)]+t*v1[2]+s*v2[2]] not in contourmatrix:
                            contourmatrix.append([X[k+1][int((j+1)/2)]+t*v1[0]+s*v2[0],Y[k+1][int((j+1)/2)]+t*v1[1]+s*v2[1],Z[k+1][int((j+1)/2)]+t*v1[2]+s*v2[2]])
            for Ypix in range(round(Y[k][int((j+1)/2)]),round(Y[k+1][int((j+1)/2)])):
                minXval=X[k][int((j+1)/2)]-(Ypix-Y[k][int((j+1)/2)])*(X[k+1][int((j+1)/2)]-X[k+1][int((j-1)/2)])/(Y[k+1][int((j+1)/2)]-Y[k][int((j+1)/2)])
                for Xpix in range(round(minXval),round(X[k][int((j+1)/2)])):
                    color=pixelcolor((Xpix,Ypix),(round(X[k+1][int((j+1)/2)]),round(Y[k+1][int((j+1)/2)])),(round(X[k][int((j+1)/2)]),round(Y[k][int((j+1)/2)])),(round(X[k+1][int((j-1)/2)]),round(Y[k+1][int((j-1)/2)])),colors[k+1][int((j+1)/2)],colors[k][int((j+1)/2)],colors[k+1][int((j-1)/2)])
                    if 0<=color[0]<=255 and 0<=color[1]<=255 and 0<=color[2]<=255:
                        scr.set_at((Xpix,Ypix),color)
    for i in contourmatrix:
        pygame.draw.circle(scr,(0,0,0),(round(i[0]),round(i[1])),1)

def squarepainter(X,Y,Z,Hcol,Mcol,Ccol,scr):
    Zmax=max(Z[0])
    Zmin=min(Z[0])
    for i in Z[1:]:
        if max(i)>Zmax:
            Zmax=max(i)
        if min(i)<Zmin:
            Zmin=min(i)
            
    colors=[]
    for i in range(len(X)):
        rowcolors=[]
        for k in range(len(X[0])):
            if Zmax!=Zmin:
                ratio=1-(Z[i][k]-Zmin)/(Zmax-Zmin)
                if ratio<=0.5:
                    dR=Mcol[0]-Hcol[0]
                    dG=Mcol[1]-Hcol[1]
                    dB=Mcol[2]-Hcol[2]
                    if dR!=0:
                        R=Mcol[0]+2*(ratio-0.5)*dR
                    else:
                        R=Mcol[0]
                    if dG!=0:
                        G=Mcol[1]+2*(ratio-0.5)*dG
                    else:
                        G=Mcol[1]
                    if dB!=0:
                        B=Mcol[2]+2*(ratio-0.5)*dB
                    else:
                        B=Mcol[2]
                elif ratio>0.5:
                    dR=Ccol[0]-Mcol[0]
                    dG=Ccol[1]-Mcol[1]
                    dB=Ccol[2]-Mcol[2]
                    if dR!=0:
                        R=Ccol[0]+2*(ratio-1)*dR
                    else:
                        R=Mcol[0]
                    if dG!=0:
                        G=Ccol[1]+2*(ratio-1)*dG
                    else:
                        G=Mcol[1]
                    if dB!=0:
                        B=Ccol[2]+2*(ratio-1)*dB
                    else:
                        B=Mcol[2]
            else:
                R=Ccol[0]
                G=Ccol[1]
                B=Ccol[2]
            rowcolors.append((R,G,B))
        colors.append(rowcolors)
        
    xlength=(X[0][-1]-X[0][0])/(len(X[0])-1)
    ylength=(Y[-1][0]-Y[0][0])/(len(X)-1)
    for i in range(len(Y)):
        for k in range(len(X[0])):
            pygame.draw.rect(scr,colors[i][k],(ceil(X[i][k]-xlength/2),ceil(Y[i][k]-ylength/2),ceil(xlength),ceil(ylength)))

screen_x=800
screen_y=700
screen=pygame.display.set_mode((screen_x,screen_y))
pygame.display.set_caption("Heat Map Generator")

pygame.font.init()
font=pygame.font.SysFont("cambria",16)

hotcolor=(205,27,30)
midcolor=(250,250,250)
coldcolor=(30,27,205)

Xmin=-1
Xmax=1
Ymin=-1
Ymax=1
nodenumber=101
func="3*x**3+2*y**2+x*y"

X=[[Xmin+(Xmax-Xmin)/(nodenumber-1)*i for i in range(nodenumber)] for k in range(nodenumber)]
Y=[[Ymin+(Ymax-Ymin)/(nodenumber-1)*k]*nodenumber for k in range(nodenumber)]
zvalues=[[eval(func) for x,y in zip(X[j],Y[j])] for j in range(nodenumber)]

Zmax=max(zvalues[0])
Zmin=min(zvalues[0])
for i in zvalues[1:]:
    if max(i)>Zmax:
        Zmax=max(i)
    if min(i)<Zmin:
        Zmin=min(i)

contourvalue=round((Zmax+Zmin)/2,1)
contourstep=(Zmax-Zmin)/100
Xstep=(Xmax-Xmin)/100
Ystep=(Ymax-Ymin)/100

font.set_bold(True)
surface_Xmax=font.render("%g"%Xmax,True,(0,0,0))
surface_Xmin=font.render("%g"%Xmin,True,(0,0,0))
surface_Ymax=font.render("%g"%Ymax,True,(0,0,0))
surface_Ymin=font.render("%g"%Ymin,True,(0,0,0))
surface_Zmax=font.render("%g"%Zmax,True,(0,0,0))
surface_Zmin=font.render("%g"%Zmin,True,(0,0,0))
surface_contourvalue=font.render("Contour@%g"%contourvalue,True,(0,0,0))
surface_xaxis=font.render("X",True,(0,0,0))
surface_yaxis=font.render("Y",True,(0,0,0))
surface_zaxis=font.render("Z",True,(0,0,0))

surface_func=font.render(func,True,(0,0,0))
surface_z=font.render("z(x,y)=",True,(0,0,0))
func_selection=False
pre_value=func
indx=len(func)-1

deltaY=Ymax-Ymin
deltaX=Xmax-Xmin

nodes_in_row=len(X[0])
row_number=len(X)

if deltaX>=deltaY:
    r=deltaY/deltaX
    xvalues=[[100+500/(nodes_in_row-1)*k for k in range(nodes_in_row)] for i in range(row_number)]
    yvalues=[[int(350-250*r+500*r/row_number*i)]*nodes_in_row for i in range(row_number)]
else:
    r=deltaX/deltaY
    xvalues=[[350-250*r+500*r/(nodes_in_row-1)*k for k in range(nodes_in_row)] for i in range(row_number)]
    yvalues=[[int(100+500/row_number*i)]*nodes_in_row for i in range(row_number)]
    
screen.fill((255,255,255),(0,0,screen_x,screen_y))
pygame.display.update()

run=True
change=True
func_change=True
vistype=1
contour=True
shiftcont=False
pan=False
panfirst=False
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        elif event.type==pygame.KEYDOWN:
            if not func_selection:
                if event.key==pygame.K_q:
                    run=False
                elif event.key==pygame.K_m:
                    vistype*=-1
                    change=True
                    func_change=True
                elif event.key==pygame.K_c:
                    contour=not contour
                    change=True
                    func_change=True
            elif func_selection and event.key==pygame.K_RETURN:
                surface_func=font.render(func,True,(0,0,0))
                surface_z=font.render("z(x,y)=",True,(0,0,0))
                func_selection=False
                if pre_value!=func:
                    try:
                        x=0.1
                        y=0.1
                        t=eval(func)
                        zvalues=[[eval(func) for x,y in zip(X[j],Y[j])] for j in range(len(X))]
                        Zmax=max(zvalues[0])
                        Zmin=min(zvalues[0])
                        for i in zvalues[1:]:
                            if max(i)>Zmax:
                                Zmax=max(i)
                            if min(i)<Zmin:
                                Zmin=min(i)
                        contourvalue=round((Zmax+Zmin)/2,1)
                        contourstep=(Zmax-Zmin)/100
                        surface_Zmax=font.render("%g"%Zmax,True,(0,0,0))
                        surface_Zmin=font.render("%g"%Zmin,True,(0,0,0))
                        surface_contourvalue=font.render("Contour@%g"%contourvalue,True,(0,0,0))
                        change=True
                        pre_value=func
                    except:
                        pass
                func_change=True
            else:
                key=pygame.key.name(event.key)
                if key=="backspace":
                    func1=func[:indx]
                    func2=func[indx+1:len(func)]
                    func=func1+func2
                    indx-=1
                    if indx<0:
                        indx=0
                    func_change=True
                elif key=="space" and surface_func.get_size()[0]+260+surface_z.get_size()[0]<screen_x:
                    func1=func[:indx+1]
                    func2=func[indx+1:len(func)]
                    func=func1+" "+func2
                    indx+=1
                    func_change=True
                elif key=="left":
                    indx-=1
                    if indx<0:
                        indx=0
                    func_change=True
                elif key=="right":
                    indx+=1
                    if indx>len(func)-1:
                        indx=len(func)-1
                    func_change=True
                elif key=="7" and shiftcont and surface_func.get_size()[0]+260+surface_z.get_size()[0]<screen_x:
                    func1=func[:indx+1]
                    func2=func[indx+1:len(func)]
                    func=func1+"/"+func2
                    indx+=1
                    func_change=True
                elif key=="8" and shiftcont and surface_func.get_size()[0]+260+surface_z.get_size()[0]<screen_x:
                    func1=func[:indx+1]
                    func2=func[indx+1:len(func)]
                    func=func1+"("+func2
                    indx+=1
                    func_change=True
                elif key=="9" and shiftcont and surface_func.get_size()[0]+260+surface_z.get_size()[0]<screen_x:
                    func1=func[:indx+1]
                    func2=func[indx+1:len(func)]
                    func=func1+")"+func2
                    indx+=1
                    func_change=True
                elif len(key)==1 and surface_func.get_size()[0]+260+surface_z.get_size()[0]<screen_x:
                    func1=func[:indx+1]
                    func2=func[indx+1:len(func)]
                    func=func1+key+func2
                    indx+=1
                    func_change=True
                elif len(key)==3 and surface_func.get_size()[0]+260+surface_z.get_size()[0]<screen_x:
                    func1=func[:indx+1]
                    func2=func[indx+1:len(func)]
                    func=func1+key[1]+func2
                    indx+=1
                    func_change=True
                elif key=="left shift" or key=="right shift":
                    shiftcont=True
                if indx!=0 and indx==len(func):
                    indx=len(func)-1
                surface_func=font.render(func,True,(50,50,250))
        elif event.type==pygame.KEYUP:
            if event.key==pygame.K_LSHIFT or event.key==pygame.K_RSHIFT:
                shiftcont=False
        elif event.type==pygame.MOUSEWHEEL:
            mousepos=pygame.mouse.get_pos()
            if not func_selection and vistype==-1 and ((deltaX>=deltaY and 100<=mousepos[0]<=600 and 350-250*r<=mousepos[1]<=350+250*r) or (deltaX<deltaY and 350-250*r<=mousepos[0]<=350+250*r and 100<=mousepos[1]<=600)):
                Xmin+=0.1*event.y*deltaX/abs(event.y)
                Xmax-=0.1*event.y*deltaX/abs(event.y)
                Ymin+=0.1*event.y*deltaY/abs(event.y)
                Ymax-=0.1*event.y*deltaY/abs(event.y)
                if Xmax-Xmin<1 or Ymax-Ymin<1:
                    Xmin-=0.1*event.y*deltaX/abs(event.y)
                    Xmax+=0.1*event.y*deltaX/abs(event.y)
                    Ymin-=0.1*event.y*deltaY/abs(event.y)
                    Ymax+=0.1*event.y*deltaY/abs(event.y)
                deltaX=Xmax-Xmin
                deltaY=Ymax-Ymin
                Xstep=(Xmax-Xmin)/100
                Ystep=(Ymax-Ymin)/100
                X=[[Xmin+(Xmax-Xmin)/(nodes_in_row-1)*i for i in range(nodes_in_row)] for k in range(row_number)]
                Y=[[Ymin+(Ymax-Ymin)/(row_number-1)*k]*nodes_in_row for k in range(row_number)]
                if deltaX>=deltaY:
                    r=deltaY/deltaX
                    xvalues=[[100+500/(nodes_in_row-1)*k for k in range(nodes_in_row)] for i in range(row_number)]
                    yvalues=[[int(350-250*r+500*r/row_number*i)]*nodes_in_row for i in range(row_number)]
                else:
                    r=deltaX/deltaY
                    xvalues=[[350-250*r+500*r/(nodes_in_row-1)*k for k in range(nodes_in_row)] for i in range(row_number)]
                    yvalues=[[int(100+500/row_number*i)]*nodes_in_row for i in range(row_number)]
                zvalues=[[eval(func) for x,y in zip(X[j],Y[j])] for j in range(len(X))]
                Zmax=max(zvalues[0])
                Zmin=min(zvalues[0])
                for i in zvalues[1:]:
                    if max(i)>Zmax:
                        Zmax=max(i)
                    if min(i)<Zmin:
                        Zmin=min(i)
                contourvalue=round((Zmax+Zmin)/2,1)
                contourstep=(Zmax-Zmin)/100
                surface_Xmax=font.render("%g"%Xmax,True,(0,0,0))
                surface_Xmin=font.render("%g"%Xmin,True,(0,0,0))
                surface_Ymax=font.render("%g"%Ymax,True,(0,0,0))
                surface_Ymin=font.render("%g"%Ymin,True,(0,0,0))
                surface_Zmax=font.render("%g"%Zmax,True,(0,0,0))
                surface_Zmin=font.render("%g"%Zmin,True,(0,0,0))
                surface_contourvalue=font.render("Contour@%g"%contourvalue,True,(0,0,0))
                change=True
                func_change=True
            else:
                maxmincont=True
                contourvalue+=contourstep*event.y
                if contourvalue>Zmax or contourvalue<Zmin:
                    contourvalue-=contourstep*event.y
                    maxmincont=False
                if maxmincont:
                    surface_contourvalue=font.render("Contour@%g"%contourvalue,True,(0,0,0))
                    change=True
                    func_change=True
        elif event.type==pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                mousepos=pygame.mouse.get_pos()
                if 250<=mousepos[0]<=250+surface_z.get_size()[0]+surface_func.get_size()[0] and screen_y-10-surface_func.get_size()[1]<=mousepos[1]<=screen_y-10 and not func_selection:
                    surface_func=font.render(func,True,(50,50,250))
                    surface_z=font.render("z(x,y)=",True,(50,50,250))
                    func_selection=True
                    func_change=True
                elif func_selection:
                    surface_func=font.render(func,True,(0,0,0))
                    surface_z=font.render("z(x,y)=",True,(0,0,0))
                    func_selection=False
                    if pre_value!=func:
                        try:
                            x=0.1
                            y=0.1
                            t=eval(func)
                            zvalues=[[eval(func) for x,y in zip(X[j],Y[j])] for j in range(len(X))]
                            Zmax=max(zvalues[0])
                            Zmin=min(zvalues[0])
                            for i in zvalues[1:]:
                                if max(i)>Zmax:
                                    Zmax=max(i)
                                if min(i)<Zmin:
                                    Zmin=min(i)
                            contourvalue=round((Zmax+Zmin)/2,1)
                            contourstep=(Zmax-Zmin)/100
                            surface_Zmax=font.render("%g"%Zmax,True,(0,0,0))
                            surface_Zmin=font.render("%g"%Zmin,True,(0,0,0))
                            surface_contourvalue=font.render("Contour@%g"%contourvalue,True,(0,0,0))
                            change=True
                            pre_value=func
                        except:
                            pass
                    func_change=True
                elif not func_selection and vistype==-1:
                    if (deltaX>=deltaY and 100<=mousepos[0]<=600 and 350-250*r<=mousepos[1]<=350+250*r) or (deltaX<deltaY and 350-250*r<=mousepos[0]<=350+250*r and 100<=mousepos[1]<=600):
                        pan=True
                        panfirst=True
        elif event.type==pygame.MOUSEBUTTONUP:
            if not pygame.mouse.get_pressed()[0] and pan:
                pan=False
    if pan:
        delx,dely=pygame.mouse.get_rel()
        if not panfirst:
            Xmax-=Xstep*delx
            Xmin-=Xstep*delx
            Ymax-=Ystep*dely
            Ymin-=Ystep*dely
            X=[[Xmin+(Xmax-Xmin)/(nodes_in_row-1)*i for i in range(nodes_in_row)] for k in range(row_number)]
            Y=[[Ymin+(Ymax-Ymin)/(row_number-1)*k]*nodes_in_row for k in range(row_number)]
            if deltaX>=deltaY:
                r=deltaY/deltaX
                xvalues=[[100+500/(nodes_in_row-1)*k for k in range(nodes_in_row)] for i in range(row_number)]
                yvalues=[[int(350-250*r+500*r/row_number*i)]*nodes_in_row for i in range(row_number)]
            else:
                r=deltaX/deltaY
                xvalues=[[350-250*r+500*r/(nodes_in_row-1)*k for k in range(nodes_in_row)] for i in range(row_number)]
                yvalues=[[int(100+500/row_number*i)]*nodes_in_row for i in range(row_number)]
            zvalues=[[eval(func) for x,y in zip(X[j],Y[j])] for j in range(len(X))]
            Zmax=max(zvalues[0])
            Zmin=min(zvalues[0])
            for i in zvalues[1:]:
                if max(i)>Zmax:
                    Zmax=max(i)
                if min(i)<Zmin:
                    Zmin=min(i)
            contourvalue=round((Zmax+Zmin)/2,1)
            contourstep=(Zmax-Zmin)/100
            surface_Xmax=font.render("%g"%Xmax,True,(0,0,0))
            surface_Xmin=font.render("%g"%Xmin,True,(0,0,0))
            surface_Ymax=font.render("%g"%Ymax,True,(0,0,0))
            surface_Ymin=font.render("%g"%Ymin,True,(0,0,0))
            surface_Zmax=font.render("%g"%Zmax,True,(0,0,0))
            surface_Zmin=font.render("%g"%Zmin,True,(0,0,0))
            surface_contourvalue=font.render("Contour@%g"%contourvalue,True,(0,0,0))
            change=True
            func_change=True
        else:
            panfirst=False
    if change:
        screen.fill((255,255,255),(0,0,screen_x,screen_y))
        for i in range(200,501):
            for k in range(30):
                ratio=(i-200)/300
                if ratio<=0.5:
                    dR=midcolor[0]-hotcolor[0]
                    dG=midcolor[1]-hotcolor[1]
                    dB=midcolor[2]-hotcolor[2]
                    if dR!=0:
                        R=midcolor[0]+2*(ratio-0.5)*dR
                    else:
                        R=midcolor[0]
                    if dG!=0:
                        G=midcolor[1]+2*(ratio-0.5)*dG
                    else:
                        G=midcolor[1]
                    if dB!=0:
                        B=midcolor[2]+2*(ratio-0.5)*dB
                    else:
                        B=midcolor[2]
                elif ratio>0.5:
                    dR=coldcolor[0]-midcolor[0]
                    dG=coldcolor[1]-midcolor[1]
                    dB=coldcolor[2]-midcolor[2]
                    if dR!=0:
                        R=coldcolor[0]+2*(ratio-1)*dR
                    else:
                        R=midcolor[0]
                    if dG!=0:
                        G=coldcolor[1]+2*(ratio-1)*dG
                    else:
                        G=midcolor[1]
                    if dB!=0:
                        B=coldcolor[2]+2*(ratio-1)*dB
                    else:
                        B=midcolor[2]
                screen.set_at((635+k,i),(R,G,B))
        screen.blit(surface_Zmax,(675,200-surface_Zmax.get_size()[1]/2))
        screen.blit(surface_Zmin,(675,500-surface_Zmin.get_size()[1]/2))
        screen.blit(surface_zaxis,(675,350-surface_zaxis.get_size()[1]/2))
        if vistype==1:
            trianglepainter(xvalues,yvalues,zvalues,hotcolor,midcolor,coldcolor,screen,contour,contourvalue)
        else:
            squarepainter(xvalues,yvalues,zvalues,hotcolor,midcolor,coldcolor,screen)
        if deltaX>=deltaY:
            screen.blit(surface_Xmax,(600-surface_Xmax.get_size()[0]/2,340-250*r-surface_Xmax.get_size()[1]))
            screen.blit(surface_Xmin,(100-surface_Xmin.get_size()[0]/2,340-250*r-surface_Xmin.get_size()[1]))
            screen.blit(surface_Ymax,(90-surface_Ymax.get_size()[0],350+250*r-surface_Ymax.get_size()[1]/2))
            screen.blit(surface_Ymin,(90-surface_Ymin.get_size()[0],350-250*r-surface_Ymin.get_size()[1]/2))
            screen.blit(surface_xaxis,(350-surface_xaxis.get_size()[0]/2,340-250*r-surface_xaxis.get_size()[1]))
            screen.blit(surface_yaxis,(90-surface_yaxis.get_size()[0],350-surface_yaxis.get_size()[1]/2))
        else:
            screen.blit(surface_Xmax,(350+250*r-surface_Xmax.get_size()[0]/2,90-surface_Xmax.get_size()[1]))
            screen.blit(surface_Xmin,(350-250*r-surface_Xmin.get_size()[0]/2,90-surface_Xmin.get_size()[1]))
            screen.blit(surface_Ymax,(340-250*r-surface_Ymax.get_size()[0],600-surface_Ymax.get_size()[1]/2))
            screen.blit(surface_Ymin,(340-250*r-surface_Ymin.get_size()[0],100-surface_Ymin.get_size()[1]/2))
            screen.blit(surface_xaxis,(350-surface_xaxis.get_size()[0]/2,90-surface_xaxis.get_size()[1]))
            screen.blit(surface_yaxis,(340-250*r-surface_yaxis.get_size()[0],350-surface_yaxis.get_size()[1]/2))
        screen.blit(surface_contourvalue,(20,screen_y-surface_contourvalue.get_size()[1]-10))
        if contour:
            pygame.draw.circle(screen,(50,250,50),(10,round(screen_y-surface_contourvalue.get_size()[1]/2-9)),4)
            pygame.gfxdraw.circle(screen,10,round(screen_y-surface_contourvalue.get_size()[1]/2-9),3,(50,250,50))
            pygame.gfxdraw.circle(screen,10,round(screen_y-surface_contourvalue.get_size()[1]/2-9),4,(50,250,50))
        else:
            pygame.draw.circle(screen,(250,50,50),(10,round(screen_y-surface_contourvalue.get_size()[1]/2-9)),4)
            pygame.gfxdraw.circle(screen,10,round(screen_y-surface_contourvalue.get_size()[1]/2-9),3,(250,50,50))
            pygame.gfxdraw.circle(screen,10,round(screen_y-surface_contourvalue.get_size()[1]/2-9),4,(250,50,50))
        change=False
    if func_change:
        pygame.draw.rect(screen,(255,255,255),(245,screen_y-15-surface_func.get_size()[1],screen_x-195,surface_func.get_size()[1]+10))
        screen.blit(surface_z,(250,screen_y-10-surface_z.get_size()[1]))
        screen.blit(surface_func,(250+surface_z.get_size()[0],screen_y-10-surface_func.get_size()[1]))
        if func_selection:
            xposition=250+surface_z.get_size()[0]
            for i in range(len(func)):
                if i<indx:
                    surface_i=font.render(func[i],True,(0,0,0))
                    xposition+=surface_i.get_size()[0]
                elif i==indx:
                    surface_i=font.render(func[i],True,(0,0,0))
                    letterwidth=surface_i.get_size()[0]
                    break
            pygame.draw.line(screen,(50,50,250),(xposition,screen_y-8),(xposition+letterwidth,screen_y-8),1)
        pygame.display.update()
        func_change=False
pygame.quit()
