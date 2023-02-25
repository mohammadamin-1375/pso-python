#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np


class PSO(object):
  """
   # klas bandi piyade sazi
  """
  def __init__(self, func, init_pos, n_particles):
    """
     aval moteqayer haye avaliye ra meqdar dehi mikonim
     moteqayer ha:
        func (function): tabe tanasob .barazandegi . baraye behine sazi
        init_pos (array-like): moqeyat avaliye baraye shiro
                               farayand behine sazi.
        n_particles (int): tedad zarat ezdeham.
    """
    self.func = func
    self.n_particles = n_particles
    self.init_pos = np.array(init_pos)
    self.particle_dim = len(init_pos)
    #moqeyat zarat ba estefade az tozi yeknavakht rah andazi mishavand
    self.particles_pos = np.random.uniform(size=(n_particles, self.particle_dim))                         * self.init_pos
    # ba estefade az toozi yeknavakht sorat zarat mishakhas mishavand
    self.velocities = np.random.uniform(size=(n_particles, self.particle_dim))

    # behtarin miqeyat ha peyda mishavand
    self.g_best = init_pos
    self.p_best = self.particles_pos

  def update_position(self, x, v):
    """
     moqeyat zarat beroz mishavand.
     zarat:
        x (array-like): moqeyat feli zare.
        v (array-like):sorat jaryan zare.
      Returns. bazgardani:
        moqeyat beroz (array-like).
    """
    x = np.array(x)
    v = np.array(v)
    new_x = x + v
    return new_x

  def update_velocity(self, x, v, p_best, g_best, c0=0.5, c1=1.5, w=0.75):
    """
     beroz resani sorat zareha.
      Args:
        x (array-like): moqeyat feli zare.
        v (array-like): sorat feli jaryan zare.
        p_best (array-like):behtarin moqeyat peyda shode baraye zare.
        g_best (array-like): behtarin moqeyat peyda shode baraye tamam zarat ta alan.
        c0 (float): meqyas shenakhti.
        c1 (float): sabet meqyas bandi omomi.
        w (float): vazn
      Returns.bazgardani:
        The updated velocity (array-like).
    """
    x = np.array(x)
    v = np.array(v)
    assert x.shape == v.shape, 'moqeyat va sorat bayad yek shekl bashand'
    # adad random beyn 0 va 1.
    r = np.random.uniform()
    p_best = np.array(p_best)
    g_best = np.array(g_best)

    new_v = w*v + c0 * r * (p_best - x) + c1 * r * (g_best - x)
    return new_v

  def optimize(self, maxiter=200):
    """
      farayand PSO ta zamani ke meyar ha baravarde shavand edame miyabad.
    hadaf be hadaqal resandan tabe hazine ast.
      maqdar ha:
          maxiter (int):hadaqal tedad tekrar qabl az tavaqof.
      Returns.bazgardani:
         behtarin meqdar yaft shode (array-like).
    """
    for _ in range(maxiter):
      for i in range(self.n_particles):
          x = self.particles_pos[i]
          v = self.velocities[i]
          p_best = self.p_best[i]
          self.velocities[i] = self.update_velocity(x, v, p_best, self.g_best)
          self.particles_pos[i] = self.update_position(x, v)
          # behtarin moqeyat baraye zare i ra beroz mikonad
          if self.func(self.particles_pos[i]) < self.func(p_best):
              self.p_best[i] = self.particles_pos[i]
          #dar kol behtarin moqeyat ra beroz mikonad
          if self.func(self.particles_pos[i]) < self.func(self.g_best):
              self.g_best = self.particles_pos[i]
    return self.g_best, self.func(self.g_best)
  
def Square(x):
  """
    In 2D: f(x,y) = x + y
  """
  return np.sum(np.square(x))

if __name__ == '__main__':
  init_pos = [1,1]
  PSO_s = PSO(func=Square, init_pos=init_pos, n_particles=50)
  res_s = PSO_s.optimize()
  print("Square function")
  print(f'x = {res_s[0]}') # x = [ 0.08355096  0.03732504 -0.00503601]
  print(f'f = {res_s[1]}') # f = 0.008399283593332805



